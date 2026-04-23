def 평균구하기(점수리스트):
    return sum(점수리스트) / len(점수리스트)


def 등급매기기(평균):
    if 평균 >= 90:
        return "A"
    elif 평균 >= 80:
        return "B"
    else:
        return "C"
