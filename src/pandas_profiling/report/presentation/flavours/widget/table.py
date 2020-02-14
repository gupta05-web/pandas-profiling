from ipywidgets import widgets, GridspecLayout, VBox

from pandas_profiling.report.formatters import fmt_color, get_fmt_mapping
from pandas_profiling.report.presentation.core.table import Table


def get_table(items):
    table = GridspecLayout(len(items), 2)
    fmt_mapping = get_fmt_mapping()
    for row_id, item in enumerate(items):
        name = item["name"]
        formatter = fmt_mapping[item["fmt"]]
        value = formatter(item["value"])
        if "alert" in item and item["alert"]:
            name = fmt_color(name, "var(--jp-error-color1)")
            value = fmt_color(value, "var(--jp-error-color1)")

        table[row_id, 0] = widgets.HTML(name)
        table[row_id, 1] = widgets.HTML(value)

    return VBox([table])


class WidgetTable(Table):
    def render(self):
        return get_table(self.content["rows"])
