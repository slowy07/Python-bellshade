"""
Pop Sort

Pop Sort merupakan metode pengurutan dengan menggunakan pendekatan Tower of Homa
yaitu mengambil nilai dari paling luar sebuah array kemudian disusun kembali
dalam array baru.
"""


def pop_sort(arr: list[int]) -> list[int]:
    # Inisialisasi data
    arr_a = arr
    arr_b = []
    arr_c = []
    print("Data sebelum disort:", arr_a, end="\n\n")

    # Kita loop hingga data di $a kosong
    while len(arr_a) > 0:
        # Keluarkan nilai paling atas dari array $a
        top = arr_a.pop()
        print("Data yang diambil:", top)
        print("Array A:", arr_a)

        # Apabila array B ada isinya dan isi paling atas dari array B
        # lebih kecil dari array A, kita pindahkan semua nilai-nilai yang
        # cocok dengan kondisi tersebut ke array C

        # Pada bagian statement kedua, anda dapat mengganti "<" menjadi ">"
        # sesuai keinginan anda.

        # Catatan:
        # Kita harus menghitung isi array terlebih dahulu sebelum mengambil
        # data array lebih utama agar menghindari error "Undefined index"
        while len(arr_b) > 0 and top > arr_b[len(arr_b) - 1]:
            arr_c.append(arr_b.pop())

        # Setelah aman, kita masukkan data dari $a ke $b
        arr_b.append(top)

        print("Array B:", arr_b)
        print("Array C:", arr_c)

        # Apabila isi $c ada, kita balikkan lagi ke $b secara berurutan.
        while len(arr_c) > 0:
            arr_b.append(arr_c.pop())

        print("Hasil sementara:", arr_b, end="\n\n")

    print("Data setelah disort:", arr_b)


if __name__ == "__main__":
    pop_sort([83, 10, 54, 92, 62, 47, 15, 72])
