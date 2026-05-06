import matplotlib
import shutil
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

cache_dir = matplotlib.get_cachedir()


def step1():
    # 캐시 폴더 경로 확인
    print(f"캐시 경로 : {cache_dir}")


def step2():
    # 캐시 삭제
    shutil.rmtree(cache_dir)
    print(f"캐시 삭제 완료 - 파이썬 재시작하기")


def step3():
    fonts = [f.name for f in fm.fontManager.ttflist]
    print("D2Coding" in fonts)
