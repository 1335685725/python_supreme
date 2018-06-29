class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def parse_from_str(date_str):
        '''
        静态方法, 采用硬编码进行初始化
        :param date_str:
        :return:
        '''
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        '''
        非硬编码来初始化对象, 就算类名改变也可以进行初始化对象
        :param date_str:
        :return:
        '''
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and int(month) > 0 and int(month) <12 and int(day) > 0 and int(day) < 31:
            return True
        else:
            return False

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return  f"{self.year}\{self.month}\{self.day}"

if __name__ == '__main__':
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()
    print(new_day)

    # 2018-12-31
    date_str = "2018-12-31"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.parse_from_str(date_str)
    print(new_day)

    # classmethod完成初始化s
    new_day = Date.from_string(date_str)
    print(new_day)

    print(Date.valid_str("2018-12-32"))