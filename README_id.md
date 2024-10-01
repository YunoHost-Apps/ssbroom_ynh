<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Scuttlebutt Room untuk YunoHost

[![Tingkat integrasi](https://dash.yunohost.org/integration/ssbroom.svg)](https://ci-apps.yunohost.org/ci/apps/ssbroom/) ![Status kerja](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Status pemeliharaan](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Pasang Scuttlebutt Room dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Scuttlebutt Room secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

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

**Versi terkirim:** 2.0.6~ynh8

**Demo:** <https://hermies.club/>

## Tangkapan Layar

![Tangkapan Layar pada Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Dokumentasi dan sumber daya

- Dokumentasi pengguna resmi: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Dokumentasi admin resmi: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Depot kode aplikasi hulu: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- Gudang YunoHost: <https://apps.yunohost.org/app/ssbroom>
- Laporkan bug: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
atau
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
