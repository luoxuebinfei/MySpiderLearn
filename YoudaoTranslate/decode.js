const crypto = require('crypto')
function g(e) {
    return crypto.createHash("md5").update(e).digest()
}


function decode1(t,o,n) {
        if (!t)
        return null;
    const a = Buffer.alloc(16, g(o))
        , c = Buffer.alloc(16, g(n))
        , i = crypto.createDecipheriv("aes-128-cbc", a, c);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
        s
}

const o = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl";
const n = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4";

function run(encode_data) {
    return (decode1(encode_data,o,n))
}

// const a = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6GBj3vx5c-AQhgqmQp7OaxBeBGdnp282rCz2waiIIATpf3fsfiq6vzU7j7ObmH1xFN_QjuDv12Pgu5TjDlCVXSlifJxAd5zN5eYWe-gfbYYJEFspKJUlnLX45JQA-iEJM8rW9NN6q4o0XysD4w_4OeztwQ4UlWW_uQ49Hh56xr2Y7UrLKW4DUCmlblMull60gvrVGtQyNEQ2veyUyBMmjpLwjNc-WJu5oycrpKFUgQDY4sYZXNIxpsHBfT1TJ9e06oPwa9vsZQ4zvgGZMIyEz0B7nFWT2H8GBVmXUoeplw2xpgYd6C8V978wUuq0TeE-g9peDMSPLH2DZ5Ewrz38YSKf_ztva81o5HsWblrhNvhg8tXou6kU6rpEEG24x21eWKfqg4wxS1aW7ZIDhVqpRJVVNEkHtONX3P7_idBPhlaupuekY2q4spyAZ4wuXO3Hkpm7r3JwYjxyMraHigvdrvl_6BF5G2VjZWxiY91LUDqWmkkFGAXq03SUU-MLjlQGsYb6td_2Zf5uSeoti1g_uwlQ_lx8GzfNvvkYYEXBj7twmZr11eJwzOklOa-rRH-gLrB02bozG8haftRASM-FT3g=="
// console.log(run(a));