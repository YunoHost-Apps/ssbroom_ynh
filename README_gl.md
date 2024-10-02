<!--
NOTA: Este README foi creado automáticamente por <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON debe editarse manualmente.
-->

# Scuttlebutt Room para YunoHost

[![Nivel de integración](https://dash.yunohost.org/integration/ssbroom.svg)](https://ci-apps.yunohost.org/ci/apps/ssbroom/) ![Estado de funcionamento](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Estado de mantemento](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Instalar Scuttlebutt Room con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Le este README en outros idiomas.](./ALL_README.md)*

> *Este paquete permíteche instalar Scuttlebutt Room de xeito rápido e doado nun servidor YunoHost.*  
> *Se non usas YunoHost, le a [documentación](https://yunohost.org/install) para saber como instalalo.*

## Vista xeral

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

**Versión proporcionada:** 2.0.6~ynh8

**Demo:** <https://hermies.club/>

## Capturas de pantalla

![Captura de pantalla de Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Documentación e recursos

- Documentación oficial para usuarias: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Documentación oficial para admin: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Repositorio de orixe do código: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- Tenda YunoHost: <https://apps.yunohost.org/app/ssbroom>
- Informar dun problema: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Info de desenvolvemento

Envía a túa colaboración á [rama `testing`](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Para probar a rama `testing`, procede deste xeito:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
ou
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Máis info sobre o empaquetado da app:** <https://yunohost.org/packaging_apps>
