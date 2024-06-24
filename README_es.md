<!--
Este archivo README esta generado automaticamente<https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
No se debe editar a mano.
-->

# Scuttlebutt Room para Yunohost

[![Nivel de integración](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![Estado funcional](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Estado En Mantención](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Instalar Scuttlebutt Room con Yunhost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Leer este README en otros idiomas.](./ALL_README.md)*

> *Este paquete le permite instalarScuttlebutt Room rapidamente y simplement en un servidor YunoHost.*  
> *Si no tiene YunoHost, visita [the guide](https://yunohost.org/install) para aprender como instalarla.*

## Descripción general

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

**Versión actual:** 2.0.6~ynh8

**Demo:** <https://hermies.club/>

## Capturas

![Captura de Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Documentaciones y recursos

- Documentación usuario oficial: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Documentación administrador oficial: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Repositorio del código fuente oficial de la aplicación : <https://github.com/ssb-ngi-pointer/go-ssb-room>
- Catálogo YunoHost: <https://apps.yunohost.org/app/ssbroom>
- Reportar un error: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Información para desarrolladores

Por favor enviar sus correcciones a la [`branch testing`](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing

Para probar la rama `testing`, sigue asÍ:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
o
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Mas informaciones sobre el empaquetado de aplicaciones:** <https://yunohost.org/packaging_apps>
