from src.apps.multi_table.gui import MultiTableSettings
from src.apps.multi_table.app import MultiTable

APPS = {
    'multi_table': {
        'name': 'Таблица умножения',
        'settings': MultiTableSettings,
        'app': MultiTable,
    }
}
