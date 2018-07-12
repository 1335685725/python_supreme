# 500G
def my_read_lines(f, new_line):
    buf = ""
    while True:
        while new_line in buf:
            pos = buf.index(new_line)
            yield buf[:pos]
            buf = buf[pos+len(new_line):]
        chunk = f.read(4096*10)
        if not chunk:
            # 说明已经读到文件结尾
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in my_read_lines(f, "{|}"):
        print(line)