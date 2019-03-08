import random
from PIL import Image,ImageDraw,ImageFont


class CheckCode(object):
    __char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __length = 4
    __size = (120, 30)
    __bg_color = (255, 255, 255)
    __flag = True

    def __init__(self):
        self.img = Image.new("RGB", self.__size, self.__bg_color)
        self.draw = ImageDraw.Draw(self.img)
        self.path = "./check_code.jpg"

    @property
    def __get_num(self):
        return random.randint(64, 200)

    @property
    def __get_color(self):
        return (self.__get_num, self.__get_num, self.__get_num)

    @property
    def __get_str(self):
        '''获取str字符串'''
        char_code = random.sample(self.__char, self.__length)
        strs = ' %s ' % ' '.join(char_code)
        return strs

    @property
    def __create_strs(self):
        '''写图片上的验证码'''
        font = ImageFont.truetype('Monaco.ttf', 18)
        strs = self.__get_str
        font_width, font_height = font.getsize(strs)
        self.draw.text(((120 - font_width) / 3, (30 - font_height) / 3), strs, font=font, fill=(0, 0, 255))
        return strs

    def get_lines(self):
        '''画干扰线'''
        n_line = (1, 3)
        line_num = random.randint(*n_line)  # 干扰线条数
        for i in range(line_num):
            begin = (random.randint(0, 120), random.randint(0, 30))
            end = (random.randint(0, 120), random.randint(0, 30))
            self.draw.line([begin, end], fill=self.__get_color)


    def get_point(self):
        '''画干扰点'''
        num = random.randint(2, 3)
        for w in range(120):
            for h in range(30):
                temp = random.randint(0, 100)
                if temp > 100 - num:
                    self.draw.point((w, h), fill=self.__get_color)

    def get_picture(self):
        if self.__flag:
            self.get_point()
            self.get_lines()
            strs = self.__create_strs
        self.img.save(self.path)
        return strs,self.path




if __name__ == '__main__':
    picture = CheckCode()
    strs, path = picture.get_picture()

    print(strs, path)
