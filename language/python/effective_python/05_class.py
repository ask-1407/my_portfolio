# 項目37 組み込み型の深い入れ子にはせずクラスを作る

# 辞書型は要素はわかっているが具体的な値がわからないものを保持するのに適している
"""
値が他の辞書や他の組み込み型の複雑な入れ子である辞書はつくらない。
完全なクラスの柔軟性が必要となる前は軽量で変更不能なデータコンテナであるnamedtupleを使う
内部状態辞書が複雑になったら記録管理コードを複数のヘルパークラスを使うように変更する
"""
class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}
    
    def report_grade(self, name, score):
        self._gradep[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)

print(book.average_grade('Isaac Newton')) # >>> 90.0

# 辞書とその関連の組み込み型は非常に使いやすいので拡張しすぎて脆弱なコードを書いてしまう危険がある
# 科目ごとに成績のリストを管理しつつ，クラスの最終的な成績に対して各点数の重みを与えて中間・最終テストの成績が重要になるようにしたい。

from collections import defaultdict
class WeightedGradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._gradesp[name] = defaultdict(list)
    
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(score, weight)

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

            return score_sum / score_count

book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein','Math',75,0.05) # 位置引数の数値が何を意味するか不明確で使い方も難しくなっている

# NOTE 記録管理が複雑になりそうだと思ったらそれをクラスに分割する。
# 分割によってデータをより良くカプセル化したインターフェースが得られるだけでなく，インターフェースと具体的な実装との間に抽象化総を設けることができる。




