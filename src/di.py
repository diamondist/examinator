from src.apps.multi_table.settings import MultiTableSettings
from src.apps.multi_table.app import MultiTable

APPS = {
    'multi_table': {
        'name': 'Таблица умножения',
        'settings': MultiTableSettings,
        'app': MultiTable,
    }
}
