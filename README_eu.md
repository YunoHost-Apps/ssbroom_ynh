<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Scuttlebutt Room YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Instalatu Scuttlebutt Room YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Scuttlebutt Room YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

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

**Paketatutako bertsioa:** 2.0.6~ynh8

**Demoa:** <https://hermies.club/>

## Pantaila-argazkiak

![Scuttlebutt Room(r)en pantaila-argazkia](./doc/screenshots/screenshot.png)

## Dokumentazioa eta baliabideak

- Erabiltzaileen dokumentazio ofiziala: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Administratzaileen dokumentazio ofiziala: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- YunoHost Denda: <https://apps.yunohost.org/app/ssbroom>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
edo
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
