data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

# Menampilkan seluruh data 
for lokasi, nama in data_panen.items():
    print(f"lokasi : {nama['nama_lokasi']} ")
    for panen, hasil in data_panen.items():
        print(f"Panen : {hasil['hasil_panen']}")


# Menampilkan jumlah hasil panen jagung dari lokasi2
hasil_lokasi2 = data_panen ['lokasi2'] ['hasil_panen'] ['jagung']
print(f"Hasil panen dari lokasi 2 yaitu: {hasil_lokasi2}")

# Menampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen ['lokasi3'] ['nama_lokasi']
print(f"Nama lokasi dari lokasi3 yaitu: {nama_lokasi3}")

# Memasukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda
hasil_padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
hasil_padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
hasil_padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
hasil_padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
hasil_padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

hasil_kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
hasil_kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
hasil_kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
hasil_kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
hasil_kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print("Jumlah hasil panen padi dan kedelai di lokasi yang berbeda:")
print(f"Kebun A  Padi: {hasil_padi_lokasi1}, Kedelai: {hasil_kedelai_lokasi1}")
print(f"Kebun B  Padi: {hasil_padi_lokasi2}, Kedelai: {hasil_kedelai_lokasi2}")
print(f"Kebun C  Padi: {hasil_padi_lokasi3}, Kedelai: {hasil_kedelai_lokasi3}")
print(f"Kebun D  Padi: {hasil_kedelai_lokasi4}, Kedelai: {hasil_kedelai_lokasi4}")
print(f"Kebun E  Padi: {hasil_kedelai_lokasi5}, Kedelai: {hasil_kedelai_lokasi5}")
