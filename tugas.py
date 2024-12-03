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
