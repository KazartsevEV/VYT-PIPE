# VYT-PIPE

Минимальный skeleton для конвейера «Вытынанка из изображения».

## Структура

```
vyt-pipe/
├─ configs/            # YAML-конфиги запусков
├─ templates/          # Заглушки шаблонов обложки/инструкций/README
├─ tools/              # Скрипты для подготовки окружения
└─ src/vyt/            # Пакет с CLI и core-модулями
```

## Быстрый старт

Быстрый запуск (PowerShell): `pwsh tools/setup_env.ps1 ; python -m vyt.cli make configs/sample.yaml`

1. Установите зависимости:
   ```powershell
   pwsh tools/setup_env.ps1
   ```
2. При желании замените входной файл: по умолчанию используется текстовый
   `input/sample.png.xbase64`, который на лету декодируется в реальный PNG.
3. Запустите CLI:
   ```bash
   python -m vyt.cli make configs/sample.yaml
   ```

CLI реализован на Typer и поддерживает команды `make`, `batch`, `qa`, `pack` (последние три пока как заглушки).

Дальнейшее развитие: заполнить модули в `src/vyt/core/` реальным функционалом согласно ТЗ.
