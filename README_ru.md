<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# Scuttlebutt Room для YunoHost

[![Уровень интеграции](https://dash.yunohost.org/integration/ssbroom.svg)](https://ci-apps.yunohost.org/ci/apps/ssbroom/) ![Состояние работы](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Состояние сопровождения](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Установите Scuttlebutt Room с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить Scuttlebutt Room быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

A Scuttlebutt room is a service for connecting scuttlebutt users.

It includes a web interface for managing who is in the room, creating invites, and creating a code of conduct for the room.

For a comprehensive introduction to rooms 2.0, watch [this video](https://www.youtube.com/watch?v=W5p0y_MWwDE).

### Features

- Rooms v1 (tunnel.connect, tunnel.endpoints, etc.)
- User management (allow- & denylisting + moderator & administrator roles), all administered via the web dashboard
- Multiple privacy modes
- Sign-in with SSB
- HTTP Invites
- Alias management

**Поставляемая версия:** 2.0.6~ynh9

**Демо-версия:** <https://hermies.club/>

## Снимки экрана

![Снимок экрана Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Документация и ресурсы

- Официальная документация пользователя: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Официальная документация администратора: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Репозиторий кода главной ветки приложения: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- Магазин YunoHost: <https://apps.yunohost.org/app/ssbroom>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
или
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
