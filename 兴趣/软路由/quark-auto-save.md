[教程地址](https://post.smzdm.com/p/arrp8oew/)
拉取
```
docker pull cp0204/quark-auto-save:latest
```

```
docker run -d \
  --name quark-auto-save \
  -p 5005:5005 \
  -e WEBUI_USERNAME=admin \
  -e WEBUI_PASSWORD=admin123 \
  -v ./quark-auto-save/config:/app/config \
  -v /etc/localtime:/etc/localtime \
  --network bridge \
  --restart unless-stopped \
  cp0204/quark-auto-save:latest
```

```
docker run -d \
  --name quark-auto-save \
  -p 5005:5005 \
  -e WEBUI_USERNAME=admin \
  -e WEBUI_PASSWORD=admin123 \
  -v /volume1/docker/quark-auto-save:/app/config \
  -v /etc/localtime:/etc/localtime \
  --network bridge \
  --restart unless-stopped \
  cp0204/quark-auto-save:latest
```


```
b-user-id=5ecbcf6b-2089-b6e4-1b93-d1c5d2fd3ab5; b-user-id=5ecbcf6b-2089-b6e4-1b93-d1c5d2fd3ab5; xlly_s=1; _UP_A4A_11_=wb96b1fe21134f85a805b20e6a404040; _UP_D_=pc; __pus=bdddd8b03bd2b08f3798fc5bfe3cfe4eAAS5eYjvVk42F5DR6pFlbzm5OQEwRGFi5h+nSAnLeJHK8+tK/gNW0B24+UIZUxD8V26m3Hic4q9uKYiiQ5ftg7Kl; __kp=3ee823b0-9f47-11ef-a753-999743703117; __kps=AATTJaOhB7zFJbw1jiCYe/DX; __ktd=MDHRAAA4yQpo6skpvgQyBw==; __uid=AATTJaOhB7zFJbw1jiCYe/DX; isg=BD8_lVA1ZEYNKWBav0ofL1KPzhPJJJPG9PtVWdEMpO414F5i2fOvFGyzJrAeuGs-; tfstk=fRRrUEqCHbhzm4lQOa5Ug85Ios5JI_m1qBsC-eYhPgjlOYpe3eTZywtW-MJFmeIkFv38nsbNW4pC-DCc0ixDP7sCZM4eAe9WYe3R-MxHYM9ShfTJy6CnfMls1UUWzZi6YT2lmtYAWwbkwlDF16CnfmwbtThN9hIhbYOHoq7CRaVHxTbcniQUxzxhqtqc7NCht6xhotb1-Wq3tg4coiQhtMxhtbxCpTwfqT090K5NjkwxBGTl058vgax_eUS4OWO23TSiTiP3tI7klOf6e5kCjdI5CGtmG75eow-5chcggsXwBe_e4bPlNKvvw_OjbPByYgBMttkguh5yYOAl3yVFZ_SVgZAiRRIXggtHat0__91D1Ofkhxn5d_7wxQKz8WxMlFORHBoamMp5Wsb6ybPVsUbh4Nqdo4rB9Lr3LTbAuGgqu49gF-XlhG2TpJB0mZSs7GwLpTbAuGgquJednxbVfVS1.; ctoken=_DZ_8uQgAms8NtkyZoablBPP; __wpkreporterwid_=ebe0e305-2b76-4ffe-141d-da02a82558ad; __itrace_wid=a61db62c-3ebd-41e5-342c-4df94ab99602; grey-id=410ff631-5c0f-4ac0-1571-398b17be647b; grey-id.sig=P2GN-2k5TEesMjqBkuSj7UzDfFqLf2b0naPJjyBS8R0; isQuark=true; isQuark.sig=hUgqObykqFom5Y09bll94T1sS9abT1X-4Df_lzgl8nM; __puus=b942004cdf1a52a5aaeda42ba50bd6d6AATAKQMOzKFpjlbAXNjuKvbHSDw9fs7ubg4xqRJ3xI473fvedjhSzpEKL/GuvM8EoKykUVmQ74ZfIz4dak/K5K7+0oiEfYDccDbZBE7kSyyGGJuykP965McuRr2xCH51P8Ugd5S8Yu/L5uyj0pnWm/5cR7PeN1RPLUDAhJ/OfKoVJ/hqqpo+8J5cNGFYrmCPvuavlt5+YdbnOayZwaLkq65k
```