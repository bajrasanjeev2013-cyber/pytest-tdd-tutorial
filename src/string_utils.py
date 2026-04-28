# class StringUtils:
#     def reverse(self, text):
#         return text[::-1]

#     def is_palindrome(self, text):
#         if not text:
#             return True
#         cleaned = text.replace(" ", "").lower()
#         return cleaned == cleaned[::-1]

#     def count_words(self, text):
#         if not text.strip():
#             return 0
#         return len(text.split())

#     def count_character(self, text, char):
#         return text.count(char)

class StringUtils:
    def reverse(self, s):
        return s[::-1]

    def is_palindrome(self, s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]

    def count_words(self, s):
        return len(s.split())