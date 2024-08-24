import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'halo aku adalah bot {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    elif message.content.startswith('$apa itu plastik?'):
        await message.channel.send("Plastik adalah salah satu makromolekul yang proses pembentukannya melalui tahap polimerisasi. Polimerisasi adalah suatu proses penggabungan dari beberapa molekul sederhana atau monomer menjadi molekul besar yang disebut makromolekul atau polimer melalui suatu proses kimia.")
    elif message.content.startswith('$sejarah plastik'):
        await message.channel.send("Sejarah plastik di muka bumi ini diawali oleh Alexander Parkes yang pertama kali memperkenalkan plastik pada sebuah eksibisi internasional di London, Inggris pada tahun 1862. Plastik temuan Parkes disebut Parkesine ini dibuat dari bahan organik dari selulosa. Parkes mengatakan bahwa temuannya ini mempunyai karakteristik mirip karet, namun dengan harga yang lebih murah. Ia juga menemukan bahwa Parkesine ini bisa dibuat transparan dan mampu dibuat dalam berbagai bentuk. Sayangnya, temuannya ini tidak bisa dimasyarakatkan karena mahalnya bahan baku yang digunakan. Kemudian pada tahun 1907 bahan sintetis pertama buatan manusia ditemukan oleh seorang ahli kimia dari New York, Leo Baekeland. Dirinya mengembangkan resin cair yang diberi nama Bakelite. Material baru ini tidak terbakar, tidak meleleh dan tidak mencair di dalam larutan asam cuka. Dengan demikian, sekali bahan ini terbentuk maka tidak akan bisa berubah. Bakelite ini bisa ditambahkan ke berbagai material lainnya seperti kayu lunak. https://id.wikipedia.org/wiki/Plastik")
    elif message.content.startswith('$cara memilah sampah'):
        await message.channel.send("1. Bedakan tempat sampah sesuai kategori agar sampah dapat didaur ulang atau digunakan kembali.    2. Kurangi penggunaan barang yang akan menjadi sampah yang tidak bisa didaur-ulang.     3. Ikut sertakan anak sejak dini untuk meningkatkan pemahaman mengenai pentingnya memilah sampah.")
    elif message.content.startswith('$apa saja jenis sampah?'):
        await message.channel.send("macam macam sampah, klasifikasi perbedaan dan karakteristik dari setiap jenis sampah yang ada. Tidak hanya terdiri dari sampah organik dan anorganik, sampah juga dapat dibedakan berdasarkan kategori tertentu. Berikut adalah uraian macam-macam sampah berdasarkan sifat, sumber, dan waktunya.")
    elif message.content.startswith('$apa itu sampah organik?'):
        await message.channel.send("Sampah organik merupakan sampah yang berasal dari sisa-sisa makhluk hidup, baik hewan, tanaman, maupun manusia yang dapat terurai secara alamiah di alam (biodegradable). Biasanya sampah jenis ini biasa kita kenal dengan sampah sisa makanan, potongan buah dan sayur, sampah dedaunan, pepohonan, dan rumput-rumputan, sekam padi, kotoran hewan ternak, juga potongan kuku dan helai rambut yang terbuang ke tanah. Sampah organik bisa dibedakan lagi secara lebih mendetail ke dalam dua jenis, yaitu sampah organik kering dan sampah organik basah. Sampah organik kering punya kandungan air yang lebih sedikit dibandingkan sampah organik basah. Oleh karena itu, biasanya sampah organik basah akan lebih cepat membusuk sehingga hancur lebih dulu.")
    elif message.content.startswith('apa itu sampah anorganik?'):
        await message.channel.send("Berbeda dari sampah organik, sampah anorganik tidak dapat terurai secara alami (undegradable) karena materialnya tidak berasal dari alam melainkan hasil olahan dari bahan sintetik tertentu. Beberapa contoh sampah anorganik yang sering dijumpai sehari-hari misalnya seperti kantong plastik, kaleng, aluminium, botol kaca, styrofoam, karton, tekstil dan masih banyak lagi. Barang-barang dengan material tersebut tidak dapat membusuk dengan bantuan alam, untuk itu harus diolah kembali oleh manusia atau mesin agar bisa dimanfaatkan menjadi produk baru.")
    #lanjutt
        
client.run("TOKEN DI VISUAL STUDIO KODE")
