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

#Membuat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
kebun_a_padi = data_panen['lokasi1']['hasil_panen']['padi']
kebun_b_padi = data_panen['lokasi2']['hasil_panen']['padi']
kebun_c_padi = data_panen['lokasi3']['hasil_panen']['padi']
kebun_d_padi = data_panen['lokasi4']['hasil_panen']['padi']
kebun_e_padi = data_panen['lokasi5']['hasil_panen']['padi']

kebun_a_kedelai = data_panen['lokasi1']['hasil_panen']['kedelai']
kebun_b_kedelai = data_panen['lokasi2']['hasil_panen']['kedelai']
kebun_c_kedelai = data_panen['lokasi3']['hasil_panen']['kedelai']
kebun_d_kedelai = data_panen['lokasi4']['hasil_panen']['kedelai']
kebun_e_kedelai = data_panen['lokasi5']['hasil_panen']['kedelai']

# Output hasil
print("Hasil Panen Padi dan Kedelai dari Setiap Lokasi:")
print(f"Kebun a Padi: {kebun_a_padi}, Kedelai: {kebun_a_kedelai}")
print(f"Kebun b Padi: {kebun_b_padi}, Kedelai: {kebun_b_kedelai}")
print(f"Kebun c Padi: {kebun_c_padi}, Kedelai: {kebun_c_kedelai}")
print(f"Kebun d Padi: {kebun_d_padi}, Kedelai: {kebun_d_kedelai}")
print(f"Kebun e Padi: {kebun_e_padi}, Kedelai: {kebun_e_kedelai}")
