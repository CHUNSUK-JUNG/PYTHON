# 출처 [https://wikidocs.net/book/4381, 파이썬 마님 엔진으로 수학 동영상 만들기]


# [01장 '마님(manim)' 소개]
# 마님(manim)은 일반 동영상 제작 툴로는 만들기 힘든 수학/과학에 쓰이는 그래프나 애니메이션을 만들 수 있게 해주는 파이썬 라이브러리입니다.
# 2,500백만명의 구독자('20.4월 기준)를 가지고 있는 유명한 수학 YouTube 채널인 3Blue1Brown에서 이 '마님'을 가지고 모든 애니메이션을 만들고 있습니다.
# manim의 약자가 mathematics animation이기에 '매님'으로 발음하는것이 맞으나 알파벳 철자그대로 '마님'으로 부르는것이 친숙하고 우리나라 고유어인 마님(상전을 높여 이르는 말)을 연상시키기도
# 해서, 이 책에서는 '마님'이라고 표기하기로 하겠습니다.
# 마님을 이용해서 어떤것을 만들 수 있고 어떤 놀라운 점이 있는지는 푸리에 변환을 설명한 아래 영상을 보면 확실히 알 수 있을것입니다. 링크: 3Blue1Brown에서 푸리에 변환을 설명한 동영상
# 파워포인트 애니메이션이나 일반 동영상 편집툴로는 만들기 힘든 그래프들을 이용해서, 관람자들의 뇌리에 직관적으로 내용이 들어오게 합니다.
# 수학이나 과학 동영상 수업을 준비하시는 분들, 기업에서 프리젠테이션을 해야는데 파워포인트로는 한계을 느끼시는 분들, 유투브 동영상을 제작하는데 동적인 그래프를 멋지게 넣고 싶은 분들은, 
# 이 마님을 이용해 보시길 권장합니다.
# 이 책에서는, 이 마님 라이브러리를 이용해서 이러한 동영상을 만들 수 있게, 처음 설치부터 최종 동영상제작까지의 방법을 설명하겠습니다.
# 파이썬 프로그래밍을 이용하기에 파이썬에 대한 기초 문법은 알고 있어야합니다. 그 나머지는 책에서 그때그때 필요한 부분을 설명할 것이기에, 그냥 설명을 따라가면 동영상 제작을 
# 할 수 있을 것입니다.


# [02장 개발환경 구축하기]
# 마님을 이용하기 위해서는 몇 가지 필수 라이브러리의 설치 및 마님 패키지 설치가 필요합니다.
# 다운로드할 파일이 좀 크기에(특히 수식입력용 라이브러이인 Miktex) 전체 다운로드 및 설치에 30분~1시간 정도 소요될겁니다.

# [02-1 기본 환경 구성 및 필수 라이브러리 설치]
# 마님은 윈도우즈뿐만아니라 리눅스와 맥(Mac)에서도 설치할 수 있으나, 여기서는 Windows7 혹은 Windows10을 사용하는 경우에 대해서만 설치방법을 소개하겠습니다.
# 기본 환경
# 운영체제: Windows 7 혹은 Windows 10
# 파이썬 버전: Python 3 (파이썬이 설치되어 있지 않다면 파이썬 사이트 참조해서 설치)
# 저자의 경우 python 3.7.7을 설치했고, 개발용 에디터로는 파이참을 이용해서 개발하고 있습니다. 어떤 에디터를 사용하더라도 개발 가능합니다.
# 필수 라이브러리 설치
# 마님은 파이썬의 기본 라이브러리외에 동영상파일 생성, 음성파일 재생, 그래픽처리, 수식문자 처리를 위한 외부 라이브러리를 사용하기에, 미리 이 라이브러리를 설치해야합니다.
# 아래 순서에 따라 설치하시면 됩니다. (파이썬은 이미 설치되어 있어야 합니다.)
# 1) FFmpeg: 동영상 파일을 생성해주는 라이브러리
# 아래 사이트에서 설치파일 받아서 설치합니다.
# https://www.wikihow.com/Install-FFmpeg-on-Windows (아래의 사이트로 연결됨)
# https://ffmpeg.org/download.html
# Windows builds from gyan.dev 선택
# https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z 다운로드 후, 압축 풀기
# 압축 해제한 폴더를 c:\bin (임의로 만든 폴더임) 폴더로 복사한다.
# win+R -> sysdm.cpl 실행하여, 환경변수에 path 설정한다.
# cmd창 실행하여, ffmpeg -version 실행하여, 아래에 다운로드 받은 파일의 버전이 표시되면 설치가 완료된 것이다.
# 2) pycairo : 그래픽 처리 라이브러리
# 아래 사이트에서 자신의 운영체제에 맞는 설치 파일을 다운로드 받아서 설치합니다. https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo
# 64비트 Windows의 경우는 ycairo‑1.19.1‑cp37‑cp37m‑win_amd64.whl 파일을 다운로드하면 됩니다. 이 파일은 파이썬 패키지를 수동으로 설치하는 패키지 파일입니다.
# 다운로드 받은 파일을 c:\bin 폴더로 복사한다.
# cdm창을 실행하여, c:\bin 폴더로 이동 후, pip3 install 명령어를 통해 설치합니다.
# pip3 install pycairo-1.20.0-cp39-cp39-win_amd64.whl
# 3) MikTex : 수식 문자 입력을 위한 LaText 프로그램
# 아래 사이트에서 설치파일 다운로드 받아 설치합니다. (약232MB로 파일이 큽니다.) https://miktex.org/download
# 만약 위 사이트에서 다운로드가 안되면 아래 사이트에서 다운로드 받아도 됩니다. http://mirrors.ibiblio.org/CTAN/systems/windows/miktex/setup/windows-x64/
# 다운로드 받은 파일 (basic-miktex-2.9.7269-x64.exe)을 실행합니다.
# 다 설치되고 나서, MikTex는 package installation을 자동으로 수행합니다. 근데, 사용하는 네트워크 환경이 porxy를 사용하는 경우 MikTex에 해당 proxy설정을 해줘야
# package installation이 가능합니다. (MikTex의 proxy설정 방법) MiKTex Console 실행 - Packages - Change - Connection Settings 에서 proxy 세팅하고, 동작하는 사이트 선택(캐나다 등)
# 4) Sox : 사운드 변환 라이브러리
# 사이트에서 설치 파일을 다운로드 받습니다. https://sourceforge.net/projects/sox/files/sox/
# 다운로드 받은 파일 (sox-14.4.2-win32.exe)을 실행해서 설치합니다.
# 필요한 라이브러리의 설치가 완료되었습니다. 이제 마님 라이브러리만 설치하면 끝납니다. 마님 라이브러리 설치는 02-2 마님 다운로드 및 설치 챕터에서 설명합니다.

# [02-2 마님 다운로드 및 설치]
# 마님(manim) 설치
# 마님용 git에서 패키지 전체 다운로드 : https://github.com/3b1b/manim
# 다운로드 받은 zip 파일을 설치할 폴더에 압축 해제:
# 예를들어 C:\bin\ 폴더에 압축해제하면 C:\bin\manim-master 폴더가 생기며 거기에 파일들 압축해제됨. - 마님에 필요한 패키지 install
# 한글 폰트 사용할 수 있게 하기 C:\bin\manim-master\manimlib\tex_templates\tex_template.tex 파일에 아래 내용 추가
# \usepackage{kotex}
# \usepackage{microtype}
# \usepackage{kotex}
# \DisableLigatures{encoding = *, family = * }
# 이렇게 하면 마님의 텍스트 표출용 클래스인 TextMobject, TexMobject, Text에 영문 대신 한글을 입력해서 사용 가능
# cmd창을 실행하여, C:\bin\manim-master 폴더로 이동 후, 아래와 같이 실행한다.
# C:\bin\manim-master> pip3  install  -r  requirements.txt
# 설치된 마님 확인
# 위와 같이 하면 마님 설치가 완료되었고, 이제 마님을 사용한 수학 애니메이션 제작이 가능합니다. 만약 동작이 안되면 마님 설치가 잘 안된 것이기에 위 마님 설치 부분을 참조해서 설치합니다.
# 설치가 제대로 되었는지는 마님 설치 폴더에서 아래와 같이 명령어를 입력해보면 됩니다.
# C:\bin\manim-master>python -m manim -h
# C:\bin\manim-master>python -m manim -h
# usage: manim.py [-h] [-p] [-w] [-s] [-l] [-m] [--high_quality] [-g] [-i] [-f]
#                 [-t] [-q] [-a] [-o FILE_NAME] [-n START_AT_ANIMATION_NUMBER]
#                 [-r RESOLUTION] [-c COLOR] [--sound] [--leave_progress_bars]
#                 [--media_dir MEDIA_DIR]
#                 [--video_dir VIDEO_DIR | --video_output_dir ...
# 마님에 디폴트로 들어 있는 샘플코드를 이용해서 동영상 하나를 만들어 봅니다.
# 아래 명령어에 의해 동영상 파일이 생성되어 자동 재생될 것입니다. 만약 도중에 에러가 나면 위의 기본 라이브러리가 제대로 설치되었는 지 확인해야합니다.
# C:\bin\manim-master>python  -m  manim  example_scenes.py  SquareToCircle  -pl
# 아래와 같은 동영상이 자동 실행될 것입니다. https://youtu.be/pBuX1mKnqgc

# [02-3 새로운 폴더에서 마님 사용하기]
# 앞 챕터에서 설치한 C:\dev\manim 폴더가 아닌 다른 폴더에서 마님을 이용한 동영상 제작을 하고자 할 때는 다음과 같이 하면 됩니다.
# 다른 폴더를 사용하고자 하는 경우가 생기는 것은, 동영상을 제작하다보면 마님 라이브러리 코드를 수정해야하는 경우가 있기에, 원본 라이브러리는 C:\dev\manim에 남겨두고, 
# 다른 폴더에서 라이브러리를 수정하고 싶은 경우가 생기기 때문입니다.
# 새로운 폴더 생성. 예를 들어 C:\now\manim
# 이 폴더로 C:\dev\manim\manimlib 폴더 전체를 복사해서 붙여넣기합니다. 즉, C:\now\manim\manimlib가 만들어지게 합니다.
# C:\dev\manim\ 폴더에 있는 2개 파일(manim.py, example_scenes.py)을 새로운 폴더(C:\now\manim\) 로 붙여넣기 합니다.
# 마님을 사용하기 위해서는 manimlib 폴더와 manim.py 만 있으면 됩니다. example_scenes.py는 잘 동작하는지 확인하기 위한 샘플코드로 필수 요소는 아닙니다.
# 제대로 동작하는지 확인해 봅니다.
# cmd 창을 열어서 C:\now\manim 폴더로 이동해서 아래와 같이 입력합니다.
# C:\now\manim>python -m manim example_scenes.py SquareToCircle -pl
# cmd 창은 윈도우 키 + R을 누르면 나타나는 실행 창에서 cmd를 치고 확인을 누르면 됩니다.
# 동영상이 동작되면 OK.
# 동영상 제작을 위한 모든 환경구성이 끝났습니다. 이제 다음 챕터에서 간단한 예제부터 시작해서 본격적으로 개발을 시작해 봅니다.


# [03장 마님 시작하기]
# 로그래밍 언어를 배울 때 가장 먼저 해보는 것이 “Hello World” 같은 간단한 문자열을 출력해보는 것입니다. 여기서도 마님을 이용해서 문자열을 출력하는 동영상을 만들어볼 것입니다. 
# 이렇게 하면, 매님이 어떻게 어떻게 동영상을 만든는지 대략 감이 잡힐 것입니다.
# 저는 프로그램 코드를 작성할 때 파이참을 이용합니다. notepad++와 Visual Studio도 사용해 보았으나, 마님을 위한 코딩을 할 때는 파이참이 제일 편했습니다.
# 이번 챕터에서는 "Hellow World" 프로그램을 notepad++와 파이참을 이용해서 어떻게 만들고 실행시키는지도 보여줍니다.

# [03-1 Hello World 만들기 (notepad++ 이용)]
# 'Hello World'라는 문자를 화면에 표출하는 동영상을 만들어 볼거고, 텍스트 에디터인 notepad++로 코드를 작성하고, 윈도우즈의 기본 명령어 입력창인 cmd를 이용해서 코드 실행을 해보겠습니다.
# notepad++가 아닌 notepad 혹은 Acroedit, Ultraedit 같은 일반적인 텍스트 에디터 사용해도 됩니다.
# 저는, 파이참을 개발환경으로 사용하길 권장합니다만, notepad++을 이용해서도 마님을 이용한 동영상 제작하는데 문제 없습니다.
# 아래는 notepad++을 사용하시려는 분만을 위한 설명으로, 파이참을 이용해서 개발하실 분은 notepad++의 설치와 notepad++ 설정변경 부분은 건너뛰고, 그 아랫 부분에 코드작성해서 실행되는 
# 모습만을 간단히 본 후, 다음 장인 03-2. Hello World 코드 및 실행방법 설명으로 넘어가시면 되겠습니다.
# notepad++ 설치
# 만약 notepad++ 프로그램이 없다면 설치합니다. notepad++ 다운로드 사이트에서 윈도우즈용 설치 프로그램을 다운로드 받아 설치하면 됩니다.
# 설치 프로그램이 원하는대로 디폴트로 선택해서 설치하면 되기에, 별도로 설치방법을 설명하지 않겠습니다.
# 사용하고 있는 윈도우즈가 32비트인지 64비트인지에 따라 32비트용 설치프로그램 혹은 64비트 설치프로그램을 선택해서 설치하시기 바랍니다.
# notepad++ 설정 변경
# 마님 개발을 위해서 notepad의 설정을 변경할 것은 없습니다. 다만, 파이썬 코딩에 있어 탭을 눌렀을 때 공백 4개로 처리하는 것이 일반적인 코딩 관습이어서, notepad의 탭 설정을 바꾸도록 합니다.
# notepad++의 탭 설정 변경 방법
# 설정 - 환경 설정 - 언어 메뉴 에서 아래 그림처럼 탭 크기를 4로 바꾸고 공백으로 바꾸기 체크
# notepad에서 마님 라이브러리를 사용하여 코딩된 파이썬 코드를 직접 실행시키지 않겠습니다.
# notepad에 NppExec 플러그인을 설치하면 notepad++ 에디터에서 바로 파이썬 코드 실행이 되도록 할 수 있으나, 마님의 경우 실행 파라미터를 계속 바꾸면서 코드에 대한 테스트가 이루어지기에, 
# 그냥 cmd 창에서 코드 실행을 하는 것이 편리할 겁니다.
# notepad++에 HelloWord 코드 작성하기
# 아래 코드를 notepad++ 편집기를 이용해 작성해 봅니다.
# from manimlib.imports import *
# class Hello_World(Scene):
#     def construct(self):
#         text=TextMobject("Hello World")
#         self.play(Write(text))
#         self.wait()
# 작성된 코드를 02장 개발환경 구축하기에서 개발 폴더로 만들어 놓은 곳에 저장합니다. 여기서는 C:\now\manim\src\hello.py 로 저장하는 것으로 하겠습니다.
# src 폴더를 새로 만들어서 거기에 파일을 저장했습니다. 이 처럼 별도 폴더를 만들어서 거기에서 작업하는 것이 파일 관리 측면에서 좋습니다.
# 실행해 보기
# cmd 창을 열어서 C:\now\manim 폴더로 이동 후, 다음과 같이 명령어를 입력해서 실행해 봅니다.
# cmd창 및 해당 폴더로 이동하는 방법을 모른다면, 02-3 새로운 폴더에서 마님 사용하기에 있는 방법 참조하기 바랍니다.
# C:\now\manim>python -m manim src\hello.py Hello_World -pl
# `Hello World' 라는 글자가 1초에 걸쳐 칠판에 써지듯이 나타나서 1초가 유지되는 동영상이 만들어 질것입니다.
''' from manimlib.imports import *
class Hello_World(Scene):
    def construct(self):
        text=TextMobject("Hello World")
        self.play(Write(text))
        self.wait() '''

# [03-2 Hello World 코드 및 실행방법 설명]
# Hello World 코드 설명
# #src\hello.py
# from manimlib.imports import *
# class Hello_World(Scene):
#     def construct(self):
#         text=TextMobject("Hello World")
#         self.play(Write(text))
#         self.wait()
# 마님에서 사용되는 여러 패키지들은 모두 manimlib\imports.py 파일내에 미리 import로 선언되어 있습니다. 그래서, 코딩할 때 from manimlib.imports import * 문구를 삽입해 놓으면, 마님에
# 사용되는 모든 모듈 및 클래스들을 사용할 수 있습니다.
# from manimlib.imports import *
# 이처럼 imports.py 파일에다가 필요한 모든 모듈들을 import를 해놓고 이 imports 파일의 모든 것을 import하는 방법은, 매번 새로운 파일을 생성해서 코딩을 할 때마다, 많은 줄에 걸쳐서
# import를 써야하는 수고를 덜어주기에, 매우 편리한 코딩 팁입니다.
# 마님에 의해 만들어지는 동영상을 만들려면 Scene를 상속받는 임의의 클래스를 만들고, construct라는 메서드를 만들어서, 그 메서드에 실행될 코드를 작성하면 됩니다.construct가 동영상 
# 실행의 main 함수 같은 역할을 담당하는 것입니다. 즉, 마님이 실행될 때 이construct 메서드가 자동으로 호출되게 됩니다.
# class Hello_World(Scene):  # 매님의 Scene 클래스를 상속받는 Hello_World 클래스 생성
#     def construct(self):   # 자동 실행되는 메서드
# 마님의 동작구조는 어떤 객체를 만들어서 좌표내에 에니매이션 효과를 넣어서 표출 하는 것입니다. 위의 Hello_World는 문자열을 포함할 수 있는 TextMobject 객체를 만들어서 이를 화면의
# 중앙에 Write라는 애니 메이션을 걸어서 객체를 화면에 표출합니다.
# #TextMobject는 문자열을 표현하는 매님의 대표적인 객제
# text=TextMobject("Hello World")
# #Scene 클래스에는 객체를 화면에 표출하는 여러 메이메이션들이 있고,
# # Write는 화면에 글자를 펜으로 쓰듯이 보여주는 애니메이션
# self.play(Write(text))
# 애니메이션을 걸어서 어떤 객체를 표출할 때는 play 메서드를 사용합니다. play 메서드는 Scene 클래스에 정의되어 있고, Hello_World 클래스가 Scene을 상속하고 있으므로, self.play를 하면 
# Scene에 있는 play 메서드가 호출될 수 있습니다.
# play 메서드는 run_time으로 실행시간이 주어지지 않으면, 디폴트로 1초가 동작합니다. 따라서, 사용된 코드인 self.play(Write(text))는 별도로 run_time이 지정되지 않았기에 1초가 
# 애니메이션이 실행됩니다.
# self.wait()는 1초간 화면이 유지됩니다. 즉, self.wait 바로 전의 화면을 유지한 채로 1초간 유지된다는 의미입니다. 여기서는 Hellow World라는 글자가 화면에 표출된 채로 1초간 유지됩니다.
# 동영상의 전체 플레이 시간을 예상해보면 2초입니다. self.play(Write(text))에 의해 1초, self.wait()에 1초 입니다. 실제 만들어진 동영상을 동작시켜보면 역시 2초짜리 동영상임을
# 알 수 있을것입니다.
# 이처럼 마님으로 동영상을 제작하다보면 몇 초짜리 동영상이 제작될 지 정확하게 프로그램으로 알 수 있고, 개발자가 그 시간을 늘리거나 줄이는 것이 간단히 run_time의 값을 조절해서 가능합니다.
# 예를 들어 위 예제에서 Hello World 글자가 화면에 써지는 시간을 5초로 늘리고 싶으면 self.play(Write(text), run_time=5) 처럼 run_time 값만 바꿔주면 됩니다.
# Hello World 실행 방법
# 작성된 src\hello.py 파일을 이용해서 동영상을 제작할 때 아래와 같은 명령어를 사용했습니다.
# C:\now\manim\python -m manim src\hello.py Hello_World -pl
# -m 옵션은, 파이썬에서 어떤 모듈을 직접 실행시키고자 할 때 사용됩니다. 이 때 해당 모듈의 '이름'만을 적어야하고 파일 확장자인 .py는 적지 않습니다. 여기서는 manim.py파일인 minim 모듈을
# 실행키는 것입니다.
# 일반적으로 python.exe에 의해 실행시키는 것은 스크립트입니다. 이 스크립트에서 여러 모듈들을 사용하는 것이고. 그런데, 이 모듈을 직접 실행시키고자 만든 것이 -m 옵션입니다. 이 옵션 뒤에 
# 모듈 이름을 적으면 해당 모듈이 실행됩니다.
# 이-m 옵션은 이러한 모듈 실행을 위한 기능외에 부수적으로 몇 가지 유용한 목적으로 사용될 수 있고, 마님에서도 여러 편리한 목적을 위해 -m 을 사용하도록 가이드되어 있습니다.
# 그러나, 위 Hello_World 처럼 일반적인 애니메이션을 만들고 이를 실행하는 데에는 -m 옵션을 붙이지 않아도 됩니다. 이 처럼 -m 옵션을 붙이지 않고 실행하는 것은, 다음 챕터에서 소개하는
# 파이참을 이용한 마님 개발에서 코드 디버깅을 하려할 때 사용됩니다.
# -m manim 다음에는 우리가 작성한 코드 파일인 hello.py가 현재 폴더에서의 상대경로와 함께 명시되어야합니다. 현재 폴더가 C:\now\manim이고 hello.py는 C:\now\manim\src 폴더에 있기에, 
# 현재 폴더를 기준으로 해서 src\hello.py 를 지정하면됩니다.
# C:\now\manim\python -m manim src\hello.py
# 이 다음에는 hello.py파일에서 우리가 만든 클래스 이름을 적게됩니다. 이는 hello.py 파일에 여러개의 클래스를 만들 수 있기 때문에, 실행할 클래스 이름을 꼭 집어서 적는 것입니다.
# 클래스 이름을 적지 않으면 어떻게 될까요?
# 만약 해당 파일에 클래스가 하나만 있다면, 그 클래스가 자동 실행됩니다. 즉, 클래스가 하나만 있다면 굳이 클래스 이름을 명시하지 않아도 됩니다.
# 클래스가 여러개 있는데 실행할 클래스 이름을 지정하지 않았다면, 그 파일에 있는 모든 클래스 이름을 번호를 붙여 보여주고, 사용자가 실행할 클래스 번호를 입력하길 기다리는 화면이 나옵니다. 
# 즉, 클래스가 여러 개 있더라도 클래스 명을 굳이 지정해서 명령어를 적지 않아도, 다시 어떤 클래스를 실행할지 물어보기에 문제 없긴합니다.
# 실행할 클래스 이름 다음에는 마님에서 지원하는 여러 옵션 들을 선택할 수 있습니다. 여기서 사용한 -pl은 Low quality의 동영상을 만들고, 동영상이 다 만들어지면 자동으로 보여주라는 옵션입니다.
# -pm은 Midium quality의 동영상을 만들고, -ps는 제일 마지막 장면을 정지영상으로해서 이미지 파일을 만듭니다.
# 만들어진 동영상 파일은 클래스이름.mp4로 저장이 되고, 이 파일은 실행하는 폴더를 기준으로해서 media\videos 폴더에 해당 모듈 이름 및 해당도별로 폴더를 달리해서 저장이됩니다.
# 위 경우는 모듈 이름이 hello이고 저해상도이기에 C:\now\manim\media\videos\hello\480p15\Hello_World.mp4 로 저장이됩니다.
# python -m manim 이라고 치면 마님에서 사용할 수 있는 옵션 파라미터에 대한 설명이 아래와 같이 나옵니다. 이 책에서 해당 옵션들이 필요할 때 그때 그때마다 필요한 것만 설명을 할 것이고, 
# 옵션에 대한 전체 설명은 별도 챕터를 만들어서 하겠습니다.
# C:\now\manim>python -m manim
# usage: manim.py [-h] [-p] [-w] [-s] [-l] [-m] [--high_quality] [-g] [-i] [-f]
#                 [-t] [-q] [-a] [-o FILE_NAME] [-n START_AT_ANIMATION_NUMBER]
#                 [-r RESOLUTION] [-c COLOR] [--sound] [--leave_progress_bars]
#                 [--media_dir MEDIA_DIR]
#                 [--video_dir VIDEO_DIR | --video_output_dir VIDEO_OUTPUT_DIR]
#                 [--tex_dir TEX_DIR] [--livestream] [--to-twitch]
#                 [--with-key TWITCH_KEY]
#                 [file] [scene_names [scene_names ...]]
# positional arguments:
#   file                  path to file holding the python code for the scene
#   scene_names           Name of the Scene class you want to see
# optional arguments:
#   -h, --help            show this help message and exit
#   -p, --preview         Automatically open the saved file once its done
#   -w, --write_to_movie  Render the scene as a movie file
#   -s, --save_last_frame
#                         Save the last frame
#   -l, --low_quality     Render at a low quality (for faster rendering)
#   -m, --medium_quality  Render at a medium quality
#   --high_quality        Render at a high quality
#   -g, --save_pngs       Save each frame as a png
#   -i, --save_as_gif     Save the video as gif
#   -f, --show_file_in_finder
#                         Show the output file in finder
#   -t, --transparent     Render to a movie file with an alpha channel
#   -q, --quiet
#   -a, --write_all       Write all the scenes from a file
#   -o FILE_NAME, --file_name FILE_NAME
#                         Specify the name of the output file, ifit should be
#                         different from the scene class name
#   -n START_AT_ANIMATION_NUMBER, --start_at_animation_number START_AT_ANIMATION_NUMBER
#                         Start rendering not from the first animation, butfrom
#                         another, specified by its index. If you passin two
#                         comma separated values, e.g. "3,6", it will endthe
#                         rendering at the second value
#   -r RESOLUTION, --resolution RESOLUTION
#                         Resolution, passed as "height,width"
#   -c COLOR, --color COLOR
#                         Background color
#   --sound               Play a success/failure sound
#   --leave_progress_bars
#                         Leave progress bars displayed in terminal
#   --media_dir MEDIA_DIR
#                         directory to write media
#   --video_dir VIDEO_DIR
#                         directory to write file tree for video
#   --video_output_dir VIDEO_OUTPUT_DIR
#                         directory to write video
#   --tex_dir TEX_DIR     directory to write tex
#   --livestream          Run in streaming mode
#   --to-twitch           Stream to twitch
#   --with-key TWITCH_KEY
#                         Stream key for twitch

# [03-3 Hello World 만들기 (파이참 이용)]
# 앞 챕터에서 살펴본 notepad++로도 마님 개발이 충분하나, 좀 더 편리하게 개발하기 위해서는 파이참(PyCham)을 사용하길 권장합니다.
# notepad++와 비교했을 때 파이참의 장점은,
# 코드 자동완성(변수 혹은 메서드의 일부부만을 타이핑했을 때 나머지 글자를 자동으로 추천해주는) 기능 뛰어남
# 어떤 함수나 메서드를 사용하고자 할 때 그 함수가 어떻게 정의되어 있는지를 봐야할 경우가 많은데, 파이참에서는 해당 함수의 이름에서 Ctrl-B를 치면 정의로 이동
# 중단점을 지정해가며 디버깅 가능
# Visual Studio도 위 기능들을 제공하는데 1)실행 옵션 지정이 파이참보다 어려움 (방법이 있을것 같은데 Visual Studio 에서 -m 옵션을 지정하며 실행시키기 힘듦) 2)블록에 대한 주석처리 
# 단축키가 불편(파이참은 Ctrl + / 을 통해 지정된 블록에 대한 주석처리가 토글되는데, Visual Studio는 불편 등의 이유로 파이참이 더 편한 듯
# 파이참(PyCham) 설치하기
# 파이참이 설치되어 있지 않다면 파이참 홈페이지에서 다운로드 받아 설치합니다.
# 설치 방법은 위키독스 책인 Python 계단밝기의 파이참(PyCharm) 설치하기 부분을 참조해서 설치하시면 편리합니다.
# 마님 개발용 파이참 프로젝트 만들기
# C:\now\manim 폴더를 마인 개발용 폴더로 사용하겠습니다. 미리 이 폴더가 존재해도 상관없으나, 이 폴더가 없다는 것으로 가정하고 설명하겠습니다.
# (1) 파이참 프로그램 실행해서 Create New Project 선택
# (2) New Project의 Location에 C:\now\manim 타이핑하고 Create 버튼 클릭
# 만일 PC에 여러 개의 python.exe 인터프리터가 있다면, 마님에 필요한 라이브러리 및 패키지가 설치된 파이썬 인터프리터를 파이참에 알려줘야합니다. 제 경우는 C:\dev\python3.7에 있는
# 인터프리터가 디폴트이고 여기에 마님에서 필요한 라이브러리들(pycairo 등)이 설치되었기에, 이것을 아래와 같이 지정해 줬습니다. 
# 설정 메뉴: File - Settings - Project: manim - Project Interpreter
# (3) 마님이 설치된 폴더에서(C:\dev\manim) 아래 파일들을 C:\now\manim 폴더로 복사/붙여넣기 수행 (윈도우즈 탐색기 이용)
#  - C:\dev\manim\manimlib 폴더 전체 --> C:\now\manim\manimlib
#  - C:\dev\manim\manim.py 파일 --> C:\now\manim\manim.py
# 이렇게 파일을 C:\nom\manim 폴더에 붙여넣기 한 후 파이참 프로젝트 창을 보면 해당 폴더와 파일이 보일것입니다.
# (4) 파이참 프로젝트 창에서 manim 프로젝트를 선택하고 마우스 우클릭 - New - Directory 선택하고, 새로 생성할 폴더 이름인 src 입력 : 이 src 폴더에 작업한 파일들을 저장할 것입니다.
# (5) 파이참에서 src 폴더를 선택하고 마우스 우클릭 - New - Python File 선택 후, New Python file 이름을 hello.py로 타이핑하고 Enter
# (6) hello.py에 아래 내용 타이핑
# from manimlib.imports import *
# class Hello_World(Scene):
#     def construct(self):
#         text=TextMobject("Hello World")
#         self.play(Write(text))
#         self.wait()
# (7) 파이참의 프로젝트 창에서 hello.py 파일이 선택된 상태에서 Ctrl-Shift-F10 누름. 파이참 프로그램의 하단부에 있는 실행창에 아래와 같은 메시지가 나오긴 하지만 동영상이 만들어지진 않을 것입니다.
# 마님 동영상을 만들게끔 Run 명령어를 수정해야합니다.
# Ctrl-Shift-F10은 선택된 파이썬 스크립트 파일을 실행하는 단축키입니다. 이렇게하면 파이참에서 해당 파일을 실행하는 Configuration을 디폴트로 만듭니다. 이렇게 만들어진 Configuration을 조금 
# 수정해서 마님용 Run Configuration을 만드는게, 맨 바닥에서 마님용 Run Configuration을 만드는것보다 편리하기 때문에 이렇게 하는 것입니다.
# (8) 파이참 메뉴에서 Run - Edit Configurations 선택
# (9) Run/Debug Configurations 다이얼로그에서 아래와 같이 입력하고 OK 버튼 클릭
# - Parameters:  `Hello_World -pl`
# - Interpreter options: `-m manim`
# - Working directory: `C:\now\manim`
# 이 Run Configuration 기능이 제가 마님 개발에 있어서 Visual Studio가 아닌 파이참을 선택하게된 결정적인 이유입니다. 편리하게 모든 실행 옵션들을 지정할 수 있게 지원합니다.
# cmd 창에서 Hello_World에 대한 동영상을 만들려면 C:\now\manim\python -m manim src\hello.py Hello_World -pl 이라고 해야합니다. 이 명령어와 동일한 효과를 나타내도록 Working directory를 
# C:\now\manim으로, python 인터프리터에 대한 옵션을 -m manim으로, 그리고 scripty path를 c:\now\manim\src\hello.py로 지정하고, 스크립트에 대한 Parameters로 Hello_World -pl 이라고 
# 지정한 것입니다.
# 나중에 고해상도의 동영상을 만들려면 다시 이 Configuration 편집창에 와서 Parameters를 Hello_World -pm으로 바꾸고 실행하면 됩니다.
# 또한 디버그가 필요한 경우는 파이참에서는 -m 옵션에 의해서 디버깅이 제대로 이루어지지 않기에, 이 경우는 Interpreter options을 -m manim이 아닌 manim 만을 입력하고 디버그를 하면 됩니다.
# (10) 파이참 메뉴에서 Run - Run 'hello 를 실행하거나 혹은 단축키로 Shift - F10을 눌러서 실행. 실행창에 아래와 같이 메시지가 나오면서 동영상 파일이 생성되고, 다 생성되면 자동으로 동영상
# 재생이 될 것입니다.
# ```
# C:\dev\python3.7\python.exe -m manim C:/now/manim/src/hello.py Hello_World -pl
# Media will be written to ./media\. You can change this behavior with the --media_dir flag.
# Writing "\centering Hello World" to ./media\Tex\d115606c2382c72c.tex
# Writing "Hello World" to ./media\Tex\7ccd9b0f9c5e13d7.tex
# File ready at C:\now\manim\media\videos\hello\480p15\Hello_World.mp4
# Played 2 animations
# Process finished with exit code 0
# ```

# [03-4 Hello Graph 만들기 (파이참 이용)]
# 마님이 가진 특별한 점은 수학에 기반을 한 그래프를 동영상으로 만드는 데 뛰어난 기능을 가지고 있다는 점입니다. 복잡하고 멋진 그래프는 차차 소개하기로하고 이번 챕터에서는 간단한 사인(sin) 
# 그래프를 그리는 동영상을 만들어 보겠습니다. 이를 통해 마님에서 어떻게 그래프를 만드는지 개략적인 윤곽을 잡을 수 있을 것입니다.
# 파이참을 실행시키고 manim 프로젝트 open
# 파이참에서 manim 프로젝트가 안만들어져 있으면 앞 챕터인 03-3 Hello World 만들기(파이참 이용)을 참조해서 manim 프로젝트를 만드시기 바랍니다.
# manim 프로젝트에서 src 폴더를 선택하고 마우스 우클릭 - New - Python File 선택하고, New Python file로hello_graph.py 타이핑하고 Enter
# hello_graph.py의 내용으로 아래 코드 타이핑
# from manimlib.imports import *
# class DrawSine(GraphScene):
#     CONFIG = {
#         "x_min" : -10,
#         "x_max" : 10,
#         "y_min" : -1.5,
#         "y_max" : 1.5,
#         "graph_origin": ORIGIN,
#     }
#     def construct(self):
#         self.setup_axes()

#         func = lambda x: np.sin(x)
#         graph = self.get_graph(func, x_min=-10,x_max=10)

#         self.play(ShowCreation(graph))
#         self.wait()
# 타이핑 에러를 줄이기 위해서, 위 내용을 복사해서 붙여넣기 하는것도 좋습니다.
# 파이참에서 Ctrl-Shift-F10 키를 눌러서 디폴트 Run Configuration 생성
# 이렇게 했을 때 에러가 없이 "Process finishe with exit code 0"라는 메시지가 나와야합니다. 그렇지 않고 에러가 발생했을 때는 해당 에러 문구를 보고 코드 작성하는데 타이핑 에러는 없는지, 
# 들여쓰기 실수는 업는지 등을 확인해서 에러를 없애고 다음 스텝으로 넘어가야합니다.
# 파이참 메뉴에서 Run - Edit Configuration 선택하고, 표출된 Run/Debug Configurations 다이얼로그 박스에서 아래 그림과 같이 수정하고 OK버튼 클릭. 수정할 곳은 
# 3군데: Parameters Interpreter options Working directory
# Shift-F10 키를 눌러서 위에서 수정한 hello_graph에 대한 Run Configuration 실행. 아래와 같은 메시지가 나오면서 동영상이 만들어지고, 만들어진 동영상이 실행되면 성공.
# C:\dev\python3.7\python.exe -m manim C:/now/manim/src/hello_graph.py DrawSine -pl
# Media will be written to ./media\. You can change this behavior with the --media_dir flag.
# File ready at C:\now\manim\media\videos\hello_graph\480p15\DrawSine.mp4
# Played 2 animations
# Process finished with exit code 0
# 동영상이 자동 실행될 때는, PC에 이미 지정되어 있는 mp4용 플레이어에서 실행됩니다. 저의 경우는 팟플레이어가 기본플레이어로 지정되어 있어서 자동 실행됩니다. 아래 그림은 실행된 모습 
# 캡처한 이미지입니다.
# DrawSine 클래스의 코드 설명
# hello_graph.py 파일에 있는 코드를 다시 적어보면 아래와 같습니다.
# from manimlib.imports import *  
# class DrawSine(GraphScene):  
#     CONFIG = {  
#         "x_min" : -10,  
#         "x_max" : 10,  
#         "y_min" : -1.5,  
#         "y_max" : 1.5,  
#         "graph_origin": ORIGIN,  
#     }  
#     def construct(self):  
#         self.setup_axes()  

#         func = lambda x: np.sin(x)  
#         graph = self.get_graph(func, x_min=-10,x_max=10)  

#         self.play(ShowCreation(graph))  
#         self.wait()
# 한 줄씩 코드 설명을 해보겠습니다.
# from manimlib.imports import *
# 마님을 사용하는 데 필요한 모든 패키지가 manimlib.imports 파일에 선언되어 있어서, 그 파일을 이런 형태로 참조하겠다고 선언하면, imports 파일에 선언된 모든 패키지를 사용할 수 있습니다. 
# 그래서, 마님용 코드를 작성할 때는 이 한 줄만 쓰면 필요한 모든 패키지를 별도 import 구문 없이 사용할 수 있습니다.
# 잠시 manimlib.imports 파일을 열어서 어떤 패키지들을 import하고 있는 지 훑어보시기 바랍니다.
# imports 파일에 보면 manimlib의 패키지 말고도 numpy os math 같은, 파이썬 코딩을 하면서 자주 쓰게되는 패키지도 미리 import 되어 있는 것을 볼 수 있습니다. 따라서 여기에 import된
# 패키지들을 별도로 import하지 않고 사용하면 됩니다.
# 특히 itertools as it, numpy as np로 되어 있음에 유의합니다. 즉, numpy.sin(x)이 아니라 np.sin(x) 로 사용합니다.
# import inspect  
# import itertools as it  
# import numpy as np  
# import operator as op  
# import os  
# import random  
# import re  
# import string  
# import sys  
# import math  
# from PIL import Image  
# from colour import Color
# class DrawSine(GraphScene):
# 마님 라이브러리에 있는 GraphScene을 상속하는 DrawSine 이라는 이름의 클래스를 선언하는 코드입니다.
# GrahpScene는 Scene의 sub-class이고, 그래프 그리기에 필요한 x축, y축 등이 미리 준비되어 있어서, 그래프가 들어간 동영상을 만들 때 유용하게 사용되는 클래스입니다. 즉, 동영상에 그래프가
# 들어간다면 이 GraphScene 클래스를 상속해서 만들면 됩니다.
# > 파이썬에서는 이처럼 어떤 클래스를 상속받는 클래스를 만들 때, 슈퍼 클래스의 이름을 괄호안에 파라미터로 명기하면됩니다.
# CONFIG = {  
#     "x_min" : -10,  
#     "x_max" : 10,  
#     "y_min" : -1.5,  
#     "y_max" : 1.5,  
#     "graph_origin": ORIGIN,  
# }
# CONFIG 딕셔너리(dictionary)는 마님에서 사용하는 특이한 방식으로, 이 CONFIG 딕셔너리에 정의한 값들을 해당 클래스의 전역 변수로 사용할 수 있습니다.
# manimlib\scene\graph_scene.py 파일을 열어보면 GraphScene 클래스에 위와 유사한 CONFIG 가 이미 정의되어 있음을 볼 수 있습니다. 이 GraphScene를 상속받은 DrawSine에서 x_min 등 일부
# 값들을 다시 재정의 했으므로, GraphScene에 정의되었던 값들이 DrawSine에서 재정의한 값으로 업데이트되게 됩니다.
# 파이썬이 데이터는 크게 3가지로 구분할 수 있습니다. 1)리스트 2)튜플 3)딕셔너리
# 3가지 데이터 유형들은 선언될 때 데이터를 감싸는 기호가 다른데, 리스트는 [ ], 튜플른 ( ), 딕셔너리는 { }를 사용합니다.
# CONFIG 딕셔너리에 정의한 값들이 해당 클래스의 전역변수가 되는 것은 마님에서 특수한 루틴을 수행하기 때문입니다. 즉, 마님의 모든 객체 클래스와 Scene 클래스의 조상이 되는 클래스가 
# Container 클래스인데, 이 클래스의 생성자에서 digest_config라는 메서드가 호출되고, 이 메서드가 각 클래스의 CONFIG 딕셔너리 값들을 읽어서 클래스의 전역변수로 만들어 줍니다.
# CONFIG 딕셔너리의 동작원리가 복잡해서 이해하기 힘들 수도 있는데, 여기서 중요한 것은 동작원리가 아니라, 이 CONFIG에 있는 값들을 재 정의해서 그래프의 필수 속성값들을 바꿀 수 있다는 것.
# 여기서는 x축의 최소/최대 값, y축의 최소/최대 값 및 화면에서 원점의 위치를 재 정의 했습니다.
# > 화면 좌표값에 대해서는 04-1 좌표계에서 다시 자세히 다룰 겁니다.
# def construct(self):
# 마님에서 main 함수의 역할을 하는 것이 construct 메서드입니다. 이 construct 메서드에 원하는 객체들을 만들고 애니메이션을 걸어서 동영상을 만들게 됩니다.
# self.setup_axes()
# GraphScene 클래스를 상속받아 클래스를 만들 때는 이 setup_axes 메서드를 호출해야만 x축, y축이 생성되서 사용가능합니다.
# func = lambda x: np.sin(x)  
# graph = self.get_graph(func, x_min=-10,x_max=10)
# 파이썬의 lambda 함수 기능을 이용해서 함수를 만들었습니다. sine 값은 numpy 라이브러리의 sin() 메서드를 사용
# lambda 기능은 파이썬에서 수학 함수를 쉽게 프로그램 함수로 만들어주는 편리한 기능입니다. lambda 키워드 뒤에 변수 명을 적고 콜론(:) 뒤에 변수와 수학 함수를 이용해서 함수 표현을 하면 됩니다.
# numpy는 파이썬에서 행렬, 벡터 등의 수학 관련 연산을 지원하는 유명한 라이브러리입니다. manimlib\imports.py 파일에 import numpy as np 라고 선언되어 있기에 numpy.sin(x)가 아닌
# np.sin(x)으로 표현 가능한 것입니다.
# 화면에 표출가능한 객체는 get_graph() 메서드를 이용해서 생성합니다. get_graph 메서드는 GraphScene 클래스에 선언되어 있는 메서드로, 메서드의 인자로 받은 func 함수를 이용해서, 화면에 
# 표출할 수 있는 마님 객체를 생성합니다. 이 때 함수가 사용할 x의 범위를 x_min과 x_max 값을 사용함으로써 지정 가능합니다.
# self.play(ShowCreation(graph))  
# self.wait()
# 생성된 graph 객체를 ShowCreation이라는 애니메이션 효과를 걸어서 화면에 1초가 표출하고, 그 다음에 1초가 유지하라는 코딩입니다.
# ShowCreation은 Write 애니메이션과 비슷한 효과인데, 객체를 화면에 나타나게할 때 일부분부터 화면에 펜으로 그리듯이 조금씩 나타나게 하는 효과를 보입니다.
# 만들어진 객체를 동영상으로 나타나게할 때, 항상 이런 패턴의 코딩을 하면됩니다. 즉, self.play를 사용하고, 이 paly의 파라미터로 어떤 애니메이션 클래스를 지정하고, 애니메이션 클래스의
# 파라미터로 객체를 지정하는 형태.
# DrawSine 클래스의 코드 일부 수정해 보기
# 위에서 작성한 DrqwSine 클래스에서 일부 코드를 수정해서 다시 동영상을 만들어 보겠습니다. 수정사항은 3가지 입니다.
# 사인 그래프의 선을 빨간색 실선으로 변환
# 애니메이션 효과를, 화면에 서서히 나타나는 FadeIn으로 변경
# 애니메이션 효과가 4초간에 걸쳐 이루어지도록.
# 그래프의 선 색을 바꾸는 것은 get_graph의 파라미터로 라인 색상을 지정하면 됩니다.
# self.get_graph( func, x_min=-10,x_max=10, color=RED)
# RED는 미리 정의되어 있는 상수 값으로, manimlib\constants.py에 미리 정의되어 있습니다.
# constants.py 파일을 실제 열어보면 RED 값에 대해 직접 지정된 것이 없습니다. RED_E, RED_D 같은 값은 지정되어 있지만.
# 그래서 이상하게 생각할 수 있는데, constants.py의 하단부에 아래와 같은 코드가 있고, 이 코드에 의해서 _E _D 값이 떨어져 나간 RED 값이 지정되는 것입니다. 즉, RED 값은 RED_C 값과 같습니다.
#   for name in [s for s in list(COLOR_MAP.keys()) if s.endswith("_C")]:  
#     locals()[name.replace("_C", "")] = locals()[name]
# 페이드인 애니메이션 효과는 FadeIn 클래스를 사용하면 됩니다. 그리고, 애니메이션이 진행되는 시간은 run_time값을 지정해서 가능
# self.play(FadeIn(graph), run_time=4)
# play 메서드에 run_time=4와 같이 파라미터를 계속해서 추가할 수 있는 것은 play 메서드가 def play(self, *args, **kwargs): 와 같이 선언되어 있기 때문에 가능한 것입니다. *args이기에 
# 여러 개의 애니메이션을 계속해서 넣을 수 있는 것이고, **kwargs 이기에 여러 개의 딕셔너리 값을 파라미터로 지정 가능한 것입니다.
# [파이썬 문법] 파이썬에서 메서드의 파라미터 변수 앞에 * 가 있는 것은, 파라미터 변수를 튜플 형태로 받겠다는 것이어서, 여러개의 변수를 파라미터로 넘길 수 있는 것이고, 별표가 두 개 있는 
# 것은 딕셔너리 형태로 여러개의 파라미터를 받겠다는 의미입니다.
# 변경된 최종 코드는 다음과 같습니다.
# from manimlib.imports import *  
# class DrawSine(GraphScene):  
#     CONFIG = {  
#         "x_min" : -10,  
#         "x_max" : 10,  
#         "y_min" : -1.5,  
#         "y_max" : 1.5,  
#         "graph_origin": ORIGIN,  
#     }  
#     def construct(self):  
#         self.setup_axes()  
#         func = lambda x: np.sin(x)  
#         graph = self.get_graph(func, x_min=-10,x_max=10, color=RED)  
#         self.play(FadeIn(graph), run_time=4)  
#         self.wait()
# 이 코드를 동영상으로 만드는 Run을 실행해보겠습니다. 파이참에서 Shift - F10 키를 누르면 동영상 파일이 생성되고, 완성되면 자동 실행 됩니다.
''' from manimlib.imports import *  
class DrawSine(GraphScene):  
    CONFIG = {  
        "x_min" : -10,  
        "x_max" : 10,  
        "y_min" : -1.5,  
        "y_max" : 1.5,  
        "graph_origin": ORIGIN,  
    }  
    def construct(self):  
        self.setup_axes()  
        func = lambda x: np.sin(x)  
        graph = self.get_graph(func, x_min=-10,x_max=10, color=RED)  
        self.play(FadeIn(graph), run_time=4)  
        self.wait() '''

# [03-5 샘플 감상하기(파이참 이용)]
# 마님 패키지를 다운로드 받으면 샘플 코드로 example_scenes.py 파일이 들어 있습니다. 여기에 여러 동영상을 만들 수 있는 샘플 코드들이 있는데, 이번 챕터에서는 이 example_scenes.py를 파이참에서
# 어떻게 실행시키는지 방법을 소개하겠습니다.
# 1.윈도우즈의 파일 탐색기를 이용해서, 다운로드한 마님 패키지에서 example_scenes.py를 C:\now\manim 폴더에 붙여넣기 합니다.
# 앞 챕터에서 파이참으로 개발환경 구축할 때, 파이참의 manim 프로젝트로 C:\now\manim 폴더를 지정했기에, C:\now\manim 폴더로 example_scenes.py 파일을 붙여넣기 하라고 한 것입니다.
# 2.파이참 실행하고 앞 챕터에서 만들었던 마님 프로젝트 Open
# 3.파이참 프로젝트 창에서 example_scenes.py 선택하고 마우스 우클릭 - Run 'example_scenes' 선택. 혹은 단축키로 Ctrl+Shift+F10 누름
# 4.파이참 메뉴에서 Run - Edit Configuration을 선택해서 아래 내용처럼 일부 항목 수정
# * Parameters: -pl
# * Interpreter options: -m manim
# 앞 장의 Hellow World 만들기나 Hello Graph 만들기에서는 src 폴더 밑에 소스코드를 뒀기에, 소스 폴더와 같은 위치로 자동 지정되는 Working diectory 값을 수동으로 C:\now\manim으로 바꿔야했지만, 
# 지금의 경우는 examplescenes.py 파일이 C:\now\manim에 있기에 자동으로 지정된 Working directory를 그대로 사용해도 됩니다.
# 즉, 마님을 실행할 때는 manim.py 파일이 있는 폴더를 Working directory로 해야합니다.
# 또한 Parameters의 값에 실행할 클래스 이름을 지정하지 않고 그냥 -pl 옵션만을 붙인것은, examples_scenes.py 안에 여러 개의 실행가능한 클래스가 있기에, 실행 시키고 나서 어떤 클래스를 
# 선택하겠다는 것입니다.
# 5.이제 Shift-F10을 눌러서 실행시키면, 아래와 같이 5개의 클래스 리스트가 출력되고 어떤 클래스 선택할 지 번호를 물어보게 됩니다. 1~5번내에서 숫자를 입력하면 해당 번호의 클래스가 동작해서, 
# 동영상이 만들어지고 Play됩니다.
# 만들어지는 동영상은 아래 링크에서도 감상할 수 있습니다.
# OpeningManimExample: https://youtu.be/GvENfT1STbc
# SquareToCircle: https://youtu.be/pBuX1mKnqgc
# UpdatersExample: https://youtu.be/wZja7ZoakFA
# WarpSquare: https://youtu.be/jkdsgIbCHFk
# WriteStuff: https://youtu.be/zVAC3hFfSAY

# [03-6 마님 구성요소 (좌표계, 객체, 애니메이션)]
# 마님에서 동영상을 만들어내는 과정은 "어떤 객체를 만들어서 그것을 화면 좌표계에 애니메이션으로 표출한다"라고 얘기할 수 있습니다.
# 예를 들어, Hello World라는 텍스트 객체를 화면의 중앙에 FadeIn 효과를 주며 표출하는 경우를 생각해보면, 객체 좌표계 애니메이션이라는 개념이 와 닿을 것입니다.
# 여기서 얘기한 객체 좌표계 애니메이션이 마님 동영상을 제작하는데 있어 가장 중요한 요소이고, 이를 이해하는 것이 동영상 제작을 이해하는 것입니다.
# 다음 장부터 이 3가지 요소인 좌표계 객체 애니메이션에 대해서 하나하나 자세히 설명하겠습니다.