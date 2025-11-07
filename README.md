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
2. Входной файл поставляется как **текстовый** `input/sample.png.xbase64`
   (декодируется на лету в реальный PNG, репозиторий остаётся без бинарников).
3. Запустите CLI:
   ```bash
   python -m vyt.cli make configs/sample.yaml
   ```

Для локальной проверки можно воспользоваться скриптом быстрой сборки:
```powershell
pwsh tools/make_sample.ps1
```

CLI реализован на Typer и поддерживает команды `make`, `batch`, `qa`, `pack` (последние три пока как заглушки).

Дальнейшее развитие: заполнить модули в `src/vyt/core/` реальным функционалом согласно ТЗ.
