## 🌟 문자열의 종류 확인

### 🍎 str.isdigit()

- **문법**: `s.isdigit()`
- **의미**: 문자열 `s`가 **비어있지 않고**, `s`의 **모든 문자**가 **숫자(digit)**이면 `True`, 아니면 `False`

**예시**

- "123".isdigit() → True
- "001".isdigit() → True
- "12.3".isdigit() → False (마침표 포함)
- "-123".isdigit() → False (부호 포함)
- "12 3".isdigit() → False (공백 포함)
- "".isdigit() → False (빈 문자열)
- "٣".isdigit() → True (유니코드 숫자도 digit로 인식될 수 있음)

**포인트**

- `+`, `-`, `.`, 공백이 섞이면 `False`
- “숫자처럼 보이는 문자(유니코드)”도 `True`가 될 수 있음

---

### 🍎 str.isalpha()

- **문법**: `s.isalpha()`
- **의미**: 문자열 `s`가 **비어있지 않고**, `s`의 **모든 문자**가 **문자(알파벳/유니코드 문자)**이면 `True`, 아니면 `False`

**예시**

- "abc".isalpha() → True
- "ABC".isalpha() → True
- "가나다".isalpha() → True (한글도 문자로 인식)
- "abc123".isalpha() → False (숫자 포함)
- "abc def".isalpha() → False (공백 포함)
- "abc!".isalpha() → False (특수문자 포함)
- "" .isalpha() → False (빈 문자열)

**포인트**

- 공백/숫자/특수문자 포함 시 `False`
- 영어 알파벳만이 아니라 한글/그리스어 등도 `True`가 될 수 있음
