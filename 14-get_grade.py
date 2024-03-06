def get_grade(s1, s2, s3):
    avg = (s1+s2+s3) / 3
    return 'A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D' if avg >= 60 else 'F'

print(get_grade(95, 90, 93))
print(get_grade(82, 85, 87))
print(get_grade(60, 82, 76))
print(get_grade(66, 62, 68))
print(get_grade(58, 59, 60))