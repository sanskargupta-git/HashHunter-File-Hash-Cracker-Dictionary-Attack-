import argparse
import hashlib

def crack_hash(hash_type, target_hash, wordlist_path):
    hash_func = getattr(hashlib, hash_type.lower(), None)
    if not hash_func:
        print("❌ Unsupported hash type. Use md5, sha1, or sha256.")
        return

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                hashed_word = hash_func(word.encode()).hexdigest()
                if hashed_word == target_hash:
                    print(f"✅ Password found: {word}")
                    return
        print("❌ Password not found in wordlist.")
    except FileNotFoundError:
        print("❌ Wordlist file not found.")

def main():
    parser = argparse.ArgumentParser(description="🔓 HashHunter – Simple Hash Cracker (MD5/SHA1/SHA256)")
    parser.add_argument("-t", "--type", required=True, help="Hash type: md5, sha1, sha256")
    parser.add_argument("-H", "--hash", required=True, help="Hash value to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    args = parser.parse_args()

    crack_hash(args.type, args.hash, args.wordlist)

if __name__ == "__main__":
    main()
