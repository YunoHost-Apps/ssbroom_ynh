<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# Scuttlebutt Room per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Installa Scuttlebutt Room con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare Scuttlebutt Room su un server YunoHost in modo semplice e veloce.*  
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica

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

**Versione pubblicata:** 2.0.6~ynh7

**Prova:** <https://hermies.club/>

## Screenshot

![Screenshot di Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Documentazione e risorse

- Documentazione ufficiale per gli utenti: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Documentazione ufficiale per gli amministratori: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Repository upstream del codice dell’app: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- Store di YunoHost: <https://apps.yunohost.org/app/ssbroom>
- Segnala un problema: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
o
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>
