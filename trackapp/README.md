# TRACKINGfrom django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'status', 'created_at', 'update_at')
    list_display_links = ('tracking_id',)
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
    search_fields = ('tracking_id', 'email')
    readonly_fields = ('created_at', 'update_at')
    ordering = ('-created_at',)
    list_per_page = 25
    empty_value_display = 'N/A'

| Option                | Description                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------- |
| `list_display`        | Fields to show as columns in the list view. Can include model fields, callables, or methods. |
| `list_display_links`  | Which columns should be clickable to go to the detail page (default: first column).          |
| `list_editable`       | Fields that can be edited directly in the list view. Must be in `list_display`.              |
| `list_select_related` | Optimizes queries for related fields (ForeignKey/OneToOne).                                  |
| `ordering`            | Default ordering of the list view (`('field',)` or `('-field',)` for descending).            |


| Option              | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| `list_filter`       | Sidebar filters for fields (choices, BooleanField, DateField, etc.)    |
| `date_hierarchy`    | Adds a date drill-down navigation (works on DateField/DateTimeField).  |
| `search_fields`     | Adds a search box; works with text fields (`CharField`, `EmailField`). |
| `filter_horizontal` | For ManyToMany fields: shows a horizontal filter widget.               |
| `filter_vertical`   | Same as above, but vertical.                                           |

| Option            | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `fields`          | Controls the order and which fields appear in the admin form. |
| `fieldsets`       | Group fields with headings and optional CSS classes.          |
| `readonly_fields` | Fields that appear in the form but **cannot be edited**.      |
| `exclude`         | Fields to exclude from the form.                              |
| `form`            | Specify a custom `forms.ModelForm` for this admin.            |


| Option                | Description                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `inlines`             | Allows editing related models inline using `admin.TabularInline` or `admin.StackedInline`. |
| `raw_id_fields`       | Displays a ForeignKey field as a raw ID input instead of a dropdown.                       |
| `autocomplete_fields` | ForeignKey/ManyToMany fields with autocomplete support.                                    |

| Option              | Description                                                |
| ------------------- | ---------------------------------------------------------- |
| `actions`           | List of admin actions available in the list view.          |
| `actions_on_top`    | Show actions at the top of the list (default: True).       |
| `actions_on_bottom` | Show actions at the bottom.                                |
| `save_on_top`       | Show Save buttons at the top of the form (default: False). |

| Option                | Description                                          |
| --------------------- | ---------------------------------------------------- |
| `model`               | Optional, reference the model explicitly if needed.  |
| `list_per_page`       | Number of records displayed per page (default: 100). |
| `empty_value_display` | Text to show for empty/null fields (default: `'-'`). |
