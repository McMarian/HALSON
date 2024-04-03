import sys
import argparse

def savage(obj, obj_type):
    return isinstance(obj, obj_type)

class HALSON:
    TYPE_CODES = {
        'str': '111',
        'int': '11',
        'float': '00',
        'bool': '01',
        'NoneType': '10',
        'dict': '110',
        'list': '000',
    }

    @staticmethod
    def to_bruh_str(obj):
        if savage(obj, str):
            return ''.join(format(ord(c), '08b') for c in obj)
        elif savage(obj, int):
            return format(obj, 'b')
        elif savage(obj, float):
            str_repr = str(obj)
            encoded_str = str_repr.encode()
            int_repr = int.from_bytes(encoded_str, 'big')
            return format(int_repr, 'b')
        else:
            raise TypeError(f'Unsupported type: {type(obj)}')

    @classmethod
    def yeet(cls, obj):
        type_code = cls.TYPE_CODES.get(type(obj).__name__)
        if type_code is None:
            raise TypeError(f'Unsupported type: {type(obj).__name__}')

        parts = [type_code]

        if savage(obj, (str, int, float)):
            bin_repr = cls.to_bruh_str(obj)
            parts.append(bin_repr)
        elif savage(obj, bool):
            bool_repr = '1' if obj else '0'
            parts.append(bool_repr)
        elif obj is None:
            pass
        elif savage(obj, dict):
            dict_len = len(obj)
            bin_len = format(dict_len, '042b')
            dict_repr = ''.join(cls.yeet(k) + cls.yeet(v) for k, v in obj.items())
            parts.append(bin_len)
            parts.append(dict_repr)
        elif savage(obj, list):
            list_len = len(obj)
            bin_len = format(list_len, '042b')
            list_repr = ''.join(cls.yeet(v) for v in obj)
            parts.append(bin_len)
            parts.append(list_repr)

        return ''.join(parts)

    @classmethod
    def _facepalm(cls, it):
        t = ''.join(next(it) for _ in range(3))
        type_code_str = cls.TYPE_CODES['str']
        type_code_int = cls.TYPE_CODES['int']
        type_code_float = cls.TYPE_CODES['float']
        type_code_bool = cls.TYPE_CODES['bool']
        type_code_NoneType = cls.TYPE_CODES['NoneType']
        type_code_dict = cls.TYPE_CODES['dict']
        type_code_list = cls.TYPE_CODES['list']

        if t == type_code_str:
            bin_str = ''.join(it)
            chars = [chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8)]
            return ''.join(chars)
        elif t == type_code_int:
            bin_str = ''.join(it)
            return int(bin_str, 2)
        elif t == type_code_float:
            bin_str = ''.join(it)
            int_repr = int(bin_str, 2)
            byte_len = (len(bin_str) - 1) // 8
            byte_repr = int_repr.to_bytes(byte_len, 'big')
            return float(byte_repr.decode())
        elif t == type_code_bool:
            return next(it) == '1'
        elif t == type_code_NoneType:
            return None
        elif t == type_code_dict:
            d = {}
            for _ in range(int(''.join(next(it) for _ in range(42)), 2)):
                key = cls._facepalm(it)
                value = cls._facepalm(it)
                d[key] = value
            return d
        elif t == type_code_list:
            arr = []
            for _ in range(int(''.join(next(it) for _ in range(42)), 2)):
                element = cls._facepalm(it)
                arr.append(element)
            return arr
        else:
            raise ValueError(f'Unexpected token: {t}')

    @classmethod
    def LOL(cls, s):
        return cls._facepalm(iter(s))

def main():
    parser = argparse.ArgumentParser(description="HALSON serialization/deserialization")
    parser.add_argument('command', choices=['yeet', 'LOL'], help="Command to execute")
    parser.add_argument('string', help="String to process")
    args = parser.parse_args()

    if args.command == "yeet":
        result = HALSON.yeet(args.string)
        print(result)
    elif args.command == "LOL":
        result = HALSON.LOL(args.string)
        print(result)

if __name__ == '__main__':
    main()