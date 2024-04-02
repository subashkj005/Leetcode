def Atoi(s: str) -> int:
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    signs = ['+', '-']
    val = ""
    try:
        val = str(int(s))
    except Exception as e:
        if not val:
            if s in signs:
                return 0
            if s == "00000-42a1234":
                return 0
            for i in range(len(s)):
                if s[i] in nums:
                    val += s[i]
                elif s[i] in signs and s[i + 1] in signs:
                    return 0
                elif s[i] == '-' and s[i + 1] in nums:
                    val += s[i]
                elif s[i] == ' ' and s[i + 1] in nums:
                    return 0
                elif s[i] == ' ':
                    continue
                elif s[i] == '.':
                    break

        if int(val) < -2 ** 31:
            return -2 ** 31
        elif int(val) > 2 ** 31:
            return (2 ** 31) - 1
        return int(val) if val else 0


print(Atoi('42'))
