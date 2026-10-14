# 实验4 的校验工具模块（由 notebook 自动生成）


def parse_student(line):
    # 把 "name,score" 形式的一行解析成字典；无效记录抛出 ValueError。
    line = line.strip()
    if not line:
        raise ValueError("空行")
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}")
    name, raw_score = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(raw_score)
    except ValueError:
        raise ValueError(f"成绩不是合法的整数: {raw_score!r}") from None
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
