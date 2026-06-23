#!/usr/bin/env python3
"""Create a simple Excel workbook for TVC storyboard and prompt tables.

Usage:
  python3 make_tvc_excel.py input.tsv output.xlsx

Input rules:
  - First row is the header.
  - Columns are separated by tabs.
  - Blank lines and lines starting with # are ignored.

The script intentionally uses only the Python standard library so it can run in
minimal Codex skill environments without installing spreadsheet dependencies.
"""

from __future__ import annotations

import html
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


MAX_COLUMN_WIDTH = 80
MIN_COLUMN_WIDTH = 10


def read_tsv(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        rows.append([cell.strip() for cell in raw_line.split("\t")])
    return rows


def column_name(index: int) -> str:
    name = ""
    while index:
        index, remainder = divmod(index - 1, 26)
        name = chr(65 + remainder) + name
    return name


def xml_escape(value: str) -> str:
    return html.escape(value, quote=False)


def inline_string_cell(ref: str, value: str, style: int) -> str:
    escaped = xml_escape(value)
    return (
        f'<c r="{ref}" t="inlineStr" s="{style}">'
        f"<is><t>{escaped}</t></is>"
        "</c>"
    )


def estimate_width(values: list[str]) -> float:
    longest = max((len(value) for value in values if value), default=MIN_COLUMN_WIDTH)
    return min(MAX_COLUMN_WIDTH, max(MIN_COLUMN_WIDTH, longest * 1.15))


def build_sheet_xml(rows: list[list[str]]) -> str:
    row_count = len(rows)
    col_count = len(rows[0])
    last_cell = f"{column_name(col_count)}{row_count}"

    columns = []
    for col_index in range(1, col_count + 1):
        values = [row[col_index - 1] for row in rows]
        width = estimate_width(values)
        columns.append(
            f'<col min="{col_index}" max="{col_index}" width="{width:.1f}" '
            'customWidth="1"/>'
        )

    sheet_rows = []
    for row_index, row in enumerate(rows, start=1):
        style = 1 if row_index == 1 else 2
        height = 24 if row_index == 1 else 120
        cells = []
        for col_index, value in enumerate(row, start=1):
            ref = f"{column_name(col_index)}{row_index}"
            cells.append(inline_string_cell(ref, value, style))
        sheet_rows.append(
            f'<row r="{row_index}" ht="{height}" customHeight="1">'
            + "".join(cells)
            + "</row>"
        )

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <dimension ref="A1:{last_cell}"/>
  <sheetViews>
    <sheetView workbookViewId="0">
      <pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>
      <selection pane="bottomLeft"/>
    </sheetView>
  </sheetViews>
  <sheetFormatPr defaultRowHeight="16"/>
  <cols>{''.join(columns)}</cols>
  <sheetData>{''.join(sheet_rows)}</sheetData>
  <autoFilter ref="A1:{last_cell}"/>
  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/>
</worksheet>
"""


def styles_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="3">
    <font><sz val="11"/><name val="Aptos"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Aptos"/></font>
    <font><sz val="10"/><name val="Aptos"/></font>
  </fonts>
  <fills count="3">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF05325F"/><bgColor indexed="64"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFD7E5EF"/></left>
      <right style="thin"><color rgb="FFD7E5EF"/></right>
      <top style="thin"><color rgb="FFD7E5EF"/></top>
      <bottom style="thin"><color rgb="FFD7E5EF"/></bottom>
      <diagonal/>
    </border>
  </borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="3">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment vertical="top" wrapText="1"/>
    </xf>
  </cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
  <dxfs count="0"/>
  <tableStyles count="0" defaultTableStyle="TableStyleMedium2" defaultPivotStyle="PivotStyleLight16"/>
</styleSheet>
"""


def workbook_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="TVC Table" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>
"""


def workbook_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""


def root_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>
"""


def content_types_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>
"""


def write_xlsx(rows: list[list[str]], path: Path) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml())
        archive.writestr("_rels/.rels", root_rels_xml())
        archive.writestr("xl/workbook.xml", workbook_xml())
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml())
        archive.writestr("xl/styles.xml", styles_xml())
        archive.writestr("xl/worksheets/sheet1.xml", build_sheet_xml(rows))


def validate_xlsx(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        required = {
            "[Content_Types].xml",
            "_rels/.rels",
            "xl/workbook.xml",
            "xl/_rels/workbook.xml.rels",
            "xl/styles.xml",
            "xl/worksheets/sheet1.xml",
        }
        missing = required - set(archive.namelist())
        if missing:
            raise ValueError(f"Missing xlsx parts: {sorted(missing)}")
        ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 make_tvc_excel.py input.tsv output.xlsx", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    rows = read_tsv(input_path)
    if not rows:
        print("Input has no rows.", file=sys.stderr)
        return 1

    width = len(rows[0])
    bad_rows = [index + 1 for index, row in enumerate(rows) if len(row) != width]
    if bad_rows:
        print(f"Rows with inconsistent column counts: {bad_rows}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_xlsx(rows, output_path)
    validate_xlsx(output_path)
    print(f"Wrote {len(rows) - 1} data rows to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
