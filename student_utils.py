# student_utils.py
def parse_student(line):
    line = line.strip()
    if not line:
        return None
    parts = line.split(",")
    if len(parts)!=2:
        raise ValueError("字段数量不对")
    name, score_str = parts
    name = name.strip()
    if len(name)==0:
        raise ValueError("姓名为空")
    try:
        sc = int(score_str.strip())
    except ValueError:
        raise ValueError("成绩不是整数")
    if not (0<= sc <=100):
        raise ValueError(f"成绩{sc}超出0‑100")
    return {"name":name, "score":sc}
