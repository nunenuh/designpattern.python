class Singleton(object):
    _instance = None

    def get_instance(self):
        if self._instance == None:
            self._instance = Singleton()
        return self._instance


s1 = Singleton()
s2 = Singleton()
s3 = s1.get_instance()
s4 = s2.get_instance()
s5 = s3.get_instance()
s6 = s4.get_instance()

print(f's1 :\t{s1}')
print(f's2 :\t{s2}')
print(f's3 :\t{s3}')
print(f's4 :\t{s4}')
print(f's5 :\t{s5}')
print(f's5 :\t{s6}')




