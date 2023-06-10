# Anagram adalah sebuah kata yang dapat
# membentuk kata lain/kalimat lain.
def anagram_check(x: str, y: str) -> str:
    # Fungsi sort disini untuk mengurutkan huruf
    # Karena anagram harus memiliki huruf yang sama
    if sorted(x) == sorted(y):
        return "Anagram"
    else:
        return "Bukan Anagram"


if __name__ == "__main__":
    print(anagram_check("silent", "listen"))  # output "Anagram"
    print(anagram_check("ignite", "gnite"))  # output "Bukan Anagram"
