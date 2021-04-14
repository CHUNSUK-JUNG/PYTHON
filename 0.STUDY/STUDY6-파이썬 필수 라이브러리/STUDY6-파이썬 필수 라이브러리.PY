# 출처 [https://wikidocs.net/book/5445, 파이썬 필수 라이브러리]


[02장 바이너리 데이터 서비스]




# [01장 텍스트 처리 서비스]

# [01-03 문자열의 차이 - diff_match_patch]
# diff_match_patch는 두 개의 파일 또는 두 개의 문자열 사이의 차이점을 보여주는 라이브러리이다.
# 설치
# pip install diff_match_patch
# 문제
# 다음과 같은 문자열이 있다.
# Life is too short, you need python.
# 위 문자열이 다음처럼 바뀌었다.
# Life is short, you need python language.
# 이 때 어떤 부분이 추가되었고 어떤 부분이 삭제되었는지를 알려주는 코드를 작성하시오.
# 풀이
# 다음은 diff_match_patch를 사용한 해법이다.
# from diff_match_patch import diff_match_patch
# before = "Life is too short, you need python."
# after = "Life is short, you need python language."
# dmp = diff_match_patch()
# diff = dmp.diff_main(before, after)
# dmp.diff_cleanupSemantic(diff)
# for d in diff:
#     print(d)
# diff_match_patch() 로 dmp객체 생성후 dmp.diff_main(before, after) 로 변경전 내용과 변경후 내용을 입력으로 diff 객체를 생성하였다.
# 이렇게 diff 객체를 생성하면 이후 dmp.diff_cleanupSemantic(diff) 와 같은 함수를 사용할 수 있게 된다.
# 출력 결과는 다음과 같다.
# (0, 'Life is ')
# (-1, 'too ')
# (0, 'short, you need python')
# (1, ' language')
# (0, '.')
# diff_cleanupSemantic은 변경단위를 튜플로 묶어서 리턴한다. 튜플의 첫번째 숫자는 다음과 같은 의미를 같는다.
# 숫자	의미
# 0	동일한 문자열
# 1	추가된 문자열
# -1	삭제된 문자열
# 따라서 출력 결과 중 (0, 'Life is ') 의 의미는 Life is 는 이전 내용과 이후 내용이 동일하다는 의미이고 (-1, 'too ')는 이전 내용에서
# too 라는 문자열이 삭제되었음을 의미한다.
''' from diff_match_patch import diff_match_patch
before = "Life is too short, you need python."
after = "Life is short, you need python language."
dmp = diff_match_patch()
diff = dmp.diff_main(before, after)
dmp.diff_cleanupSemantic(diff)
for d in diff:
    print(d) '''

# [01-02 문자열 줄바꿈 - textwrap.wrap]
# textwrap.wrap은 문자열을 특정길이에 맞게 줄바꿈(wrapping)할 수 있게 해주는 파이썬 표준 라이브러리이다. 
# 문자열 래핑은 문자열이 너무 길어질 경우 특정 길이에서 줄바꿈을 하려고 할때 필요하다.
# 문제
# 다음과 같이 긴 문자열 long_text가 있다.
# >>> long_text = 'Life is too short, you need python. ' * 10
# >>> long_text
# 'Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. '
# long_text를 70바이트 길이로 줄바꿈 하시오.
# 풀이
# import textwrap
# long_text = 'Life is too short, you need python. ' * 10
# result = textwrap.wrap(long_text, width=70)
# print(result)
# 출력결과는 다음과 같다.
# ['Life is too short, you need python. Life is too short, you need', 'python. Life is too short, you need python. Life is too short, you', 'need python. Life is too short, you need python. Life is too short,', 'you need python. Life is too short, you need python. Life is too', 'short, you need python. Life is too short, you need python. Life is', 'too short, you need python.']
# textwrap.wrap 함수는 긴 문자열을 매개변수 width로 전달한 70바이트 길이만큼 잘라서 리스트로 리턴해 준다. 이것을 고정폭 문자열로 표시하려면 다음과 같이 하면 된다.
# '\n'.join(result)
# 하지만 textwrap.fill 함수를 사용하면 다음처럼 이 과정을 축약할 수 있다.
# import textwrap
# long_text = 'Life is too short, you need python. ' * 10
# result = textwrap.fill(long_text, width=70)
# print(result)
# 출력결과는 다음과 같다.
# Life is too short, you need python. Life is too short, you need
# python. Life is too short, you need python. Life is too short, you
# need python. Life is too short, you need python. Life is too short,
# you need python. Life is too short, you need python. Life is too
# short, you need python. Life is too short, you need python. Life is
# too short, you need python.
''' import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)
print(result)
import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.fill(long_text, width=70)
print(result) '''

# [01-01 문자열 말줄임 - textwrap.shorten]
# textwrap.shorten은 문자열을 특정길이에 맞게 말줄임(...)을 할 수 있도록 도와주는 파이썬 표준 라이브러리이다.
# 문제
# 다음 문자열을 길이 15자리가 넘지 않도록 말줄임하여 표시하시오. (단, 길이가 15자리가 넘지 않을 경우에는 그대로 표시)
# Life is too short, you need python
# 풀이
# import textwrap
# result = textwrap.shorten("Life is too short, you need python", width=15)
# print(result)
# 결과는 다음과 같다.
# Life is [...]
# 이 때 문자열에 포함된 모든 연속된 공백 문자열은 단일 공백 문자열로 축약된다. 그리고 매개변수 width에 전달된 길이만큼 문자열이 표시된다. 이 때 축약된 문자열을 의미하는 [...] 문자 역시 길이에 포함되며 줄여지는 문자열은 단어단위로 길이에 맞게 생략된다.
# 한글 문자열인 경우도 다음처럼 동일하게 수행된다. 단, 한글 1문자도 역시 길이 1로 계산된다는 점에 유의하자.
# import textwrap
# result = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15)
# print(result)
# 결과는 다음과 같다.
# 인생은 짧으니 [...]
# 활용예
# 코딩도장의 문제 요약중 내용이 많을 경우 다음처럼 말줄임으로 표시한다. textwrap.shorten 을 사용하면 이런 화면을 쉽게 만들수 있다.
''' import textwrap
result = textwrap.shorten("Life is too short, you need python", width=15)
print(result)
import textwrap
result = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15)
print(result) '''