#coding:shift-jis
state=["�d�Ԃɏ���Ă��ĖړI�n�ɒ������̂ɁA�]��ɂ�����łč~����Ȃ��������Ƃ�����B",
       "�҂����킹�ɘA���������ɁA�R���Ԉȏ�l��҂��������Ƃ�����B",
       "��肽�����Ȃ��̂ɁA�w���ψ�������炳�ꂽ���Ƃ�����B",
       "���Ȃ��͓V���ו��B���Ԃ̖ڂȂ�ċC�ɂ��Ȃ��I���������Ă������Ȃ��|�̐S���������Ă���I",
       "���Ȃ��̐��i�͂������ĕ��ʁB����ɔz�������}����Ƃ���̓L�`����}����B���[���l�I",
       "���Ȃ��͏��S�ҁB��Ɋ��ɗ�����܂���A�C�������痧�������Ȃ�Ă�������イ�����ˁB"]
print("1:yes 2:no")

print(state[0])

while True:
    print("�w�肳�ꂽ�����őI�������Ȃ���")
    a = input()
    if (a == "1"):
        whileTrue:
            print(state[2])
            print("1:yes 2:no")
            print("�w�肳�ꂽ�����őI�������Ȃ���")
            b = input()
            if (b == "1"):
                print(state[5])
                break
            elif (b == "2"):
                print(state[4])
                break
    elif (a == "2"):
        print(state[1])
        print("1:yes 2:no")
        print("�w�肳�ꂽ�����őI�������Ȃ���")
        c = input()
        if (c == "1"):
            print(state[3])
            break
        elif (c == "2"):
            print(state[4])
            break
    else:
        continue