class 사람 {
    String 이름;

    public 사람(String 이름) {
        this.이름 = 이름
    }
}

class 학생 extends 사람 {
    String 학교;

    public 학생(String 이름, String 학교) {
        super(이름);
        this.학교 = 학교;
    }
}

