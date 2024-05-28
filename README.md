# ZalpScript Interpreter

ZalpScript는 난해한 프로그래밍 언어입니다. 이 인터프리터는 ZalpScript 코드를 해석하고 실행할 수 있습니다.

## 주요 명령어

- `z`: 포인터 증가
- `m`: 포인터 감소
- `a`: 포인터가 가리키는 바이트의 값을 증가
- `l`: 포인터가 가리키는 바이트의 값을 감소
- `p`: 텍스트 아스키 아트 출력
- `q`: 곱하기 (포인터가 가리키는 값을 다음 값과 곱함)
- `w`: 포인터를 0으로 리셋
- `e`: 포인터가 가리키는 바이트의 값을 0으로 리셋
- `v`: 변수
- `<,>`: 반복문

## 설치 및 실행

### 요구 사항

- Python 3.x
- PyInstaller (exe 파일 생성을 위해 필요)

### 인터프리터 실행 방법

1. 프로젝트를 클론하거나 다운로드합니다.

   ```sh
   git clone https://github.com/yourusername/ZalpScript.git
   cd ZalpScript
   ```

2. 인터프리터를 실행합니다.

   ```sh
   python interpreter.py example.zalp
   ```

### exe 파일 생성 방법

1. PyInstaller를 설치합니다.

   ```sh
   pip install pyinstaller
   ```

2. exe 파일을 생성합니다.

   ```sh
   pyinstaller --onefile interpreter.py
   ```

3. `dist` 폴더에서 `interpreter.exe` 파일을 찾습니다. 이제 이 파일을 실행하여 ZalpScript 인터프리터를 사용할 수 있습니다.

### 사용 예시

다음은 간단한 ZalpScript 예제 파일 (`example.zalp`)입니다:

```
zaaapzqzzap
```

이 파일은 포인터를 증가시키고 값을 변경하며 ASCII 문자를 출력하는 예제입니다.

### 기여

1. 포크(Fork)하고 자신의 브랜치(Branch)에서 작업하세요:

   ```sh
   git checkout -b my-feature-branch
   ```

2. 변경 사항을 커밋하세요:

   ```sh
   git commit -m 'Add some feature'
   ```

3. 브랜치를 푸시(Push)하세요:

   ```sh
   git push origin my-feature-branch
   ```

4. 풀 리퀘스트(Pull Request)를 제출하세요.

### 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.