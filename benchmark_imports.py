import timeit
import json
import ast
import sys

def with_import():
    content_str = '{"type": "DASHBOARD_UPDATE", "data": {}}'
    import json as _json
    import ast as _ast
    try:
        output_dict = _json.loads(content_str)
    except:
        try:
            output_dict = _ast.literal_eval(content_str)
        except:
            pass

def without_import():
    content_str = '{"type": "DASHBOARD_UPDATE", "data": {}}'
    try:
        output_dict = json.loads(content_str)
    except:
        try:
            output_dict = ast.literal_eval(content_str)
        except:
            pass

if __name__ == "__main__":
    n = 100000
    t1 = timeit.timeit(with_import, number=n)
    t2 = timeit.timeit(without_import, number=n)
    print(f"With local imports (100k iterations): {t1:.4f}s")
    print(f"Without local imports (100k iterations): {t2:.4f}s")
    print(f"Improvement: {(t1-t2)/t1*100:.2f}%")
    print(f"Average time saved per call: {(t1-t2)/n*1e6:.4f} microseconds")
