from lzma import is_check_supported
from slider.beatmap import HoldNote, Circle, Position, Beatmap, HitObject
from os import path
from mainui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox, QProgressBar
import sys


# osu = Beatmap.from_file(f)
# osu.circle_size = 7
# osu.version += ' 4kto7k'
# new_hitobjects: list[HitObject] = []

# print(new_osu)
# new_osu.write_file(open(path.join(path.dirname(path.abspath(fn)), new_osu.display_name)+'.osu', 'w', encoding='utf-8-sig'))


class MainWin(QMainWindow, Ui_MainWindow):
    osu: Beatmap = None
    filename: str = ''
    new_osu: Beatmap = None
    new_filename: str = ''
    tmp_hitobjects: list[HitObject] = []

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.open_osu_file)
        self.info.triggered.connect(self.osu_info)
        self.convert_button.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.clear)
        self.progressbar = QProgressBar(self)
        self.statusbar.addPermanentWidget(self.progressbar)

    def clear(self):
        self.label.clear()
        self.osu = None
        self.filename = ''

    def open_osu_file(self):
        filename = QFileDialog.getOpenFileName(
            self, '打开osu文件', './', 'OSU file (*.osu)')
        if filename[0]:
            self.filename = filename[0]
            self.label.setText(path.basename(self.filename))
            with open(self.filename, 'r', encoding='utf-8-sig') as f:
                self.osu = Beatmap.from_file(f)

    def check_mania(self):
        if self.osu.mode != 3:
            QMessageBox.warning(self, '警告', '不是mania模式的文件，请重新选择')
            self.osu = None
            self.filename = ''
            self.label.clear()

    def osu_info(self):
        if self.osu:
            message = ''
            message += f'模式: {self.osu.mode}\n'
            message += f'标题: {self.osu.title}\n'
            message += f'艺术家: {self.osu.artist}\n'
            message += f'做谱者: {self.osu.creator}\n'
            message += f'版本名: {self.osu.version}\n'
            message += f'键数: {self.osu.circle_size}\n'
            message += f'HP: {self.osu.hp_drain_rate}\n'
            message += f'OD: {self.osu.overall_difficulty}\n'
            message += f'bpm: {self.osu.bpm_min()}-{self.osu.bpm_max()}'
            QMessageBox.information(self, '文件信息', message)

    def convert(self):
        if self.osu:
            if self.osu.circle_size != 4:
                QMessageBox.warning(self, '警告', '不是4key文件，请重新选择')
            else:
                if self._1_3.isChecked():
                    self._c_1_3(self.lockhand.isChecked())
                    self.save_file()
                elif self._1_2.isChecked():
                    self._c_1_2(self.lockhand.isChecked())
                    self.save_file()
                elif self._2_3.isChecked():
                    self._c_2_3(self.lockhand.isChecked())
                    self.save_file()

    def _c_1_2(self, lockhand: bool = False):
        pass

    def _c_2_3(self, lockhand: bool = False):
        pass

    def _c_1_3(self, lockhand: bool = False):
        if lockhand:
            self.tmp_hitobjects.append(HoldNote(Position(
                109, 192), self.osu._hit_object_times[0], 0, self.osu._hit_object_times[-1]))
            self.tmp_hitobjects.append(HoldNote(Position(
                402, 192), self.osu._hit_object_times[0], 0, self.osu._hit_object_times[-1]))
            self.tmp_hitobjects.append(HoldNote(Position(
                256, 192), self.osu._hit_object_times[0], 0, self.osu._hit_object_times[-1]))
        progressbar_value = 0
        for hit in self.osu._hit_objects:
            QApplication.processEvents()
            if hit.__class__ == HoldNote:
                if hit.position.x == 64:
                    self.tmp_hitobjects.append(HoldNote(Position(
                        36, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 192 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            109, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                elif hit.position.x == 192:
                    self.tmp_hitobjects.append(HoldNote(Position(
                        182, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 320 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            256, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    elif self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 64 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            109, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                elif hit.position.x == 320:
                    self.tmp_hitobjects.append(HoldNote(Position(
                        329, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 448 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            402, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    elif self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 192 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            256, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                elif hit.position.x == 448:
                    self.tmp_hitobjects.append(HoldNote(Position(
                        475, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 320 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(HoldNote(Position(
                            402, hit.position.y), hit.time, hit.hitsound, hit.end_time, hit.addition))
            elif hit.__class__ == Circle:
                if hit.position.x == 64:
                    self.tmp_hitobjects.append(
                        Circle(Position(36, hit.position.y), hit.time, hit.hitsound, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 192 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(
                            Circle(Position(109, hit.position.y), hit.time, hit.hitsound, hit.addition))
                elif hit.position.x == 192:
                    self.tmp_hitobjects.append(Circle(Position(
                        182, hit.position.y), hit.time, hit.hitsound, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 320 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(Circle(Position(
                            256, hit.position.y), hit.time, hit.hitsound,  hit.addition))
                    elif self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 64 and not lockhand:
                        print('未锁手')
                        self.tmp_hitobjects.append(
                            Circle(Position(109, hit.position.y), hit.time, hit.hitsound, hit.addition))
                elif hit.position.x == 320:
                    self.tmp_hitobjects.append(Circle(Position(
                        329, hit.position.y), hit.time, hit.hitsound, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 448 and not lockhand:
                        self.tmp_hitobjects.append(Circle(Position(
                            402, hit.position.y), hit.time, hit.hitsound,  hit.addition))
                    elif self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 192 and not lockhand:
                        self.tmp_hitobjects.append(Circle(Position(
                            256, hit.position.y), hit.time, hit.hitsound,  hit.addition))
                elif hit.position.x == 448:
                    self.tmp_hitobjects.append(Circle(Position(
                        475, hit.position.y), hit.time, hit.hitsound, hit.addition))
                    if self.osu.closest_hitobject(hit.time).time == hit.time and self.osu.closest_hitobject(hit.time).position.x == 320 and not lockhand:
                        self.tmp_hitobjects.append(Circle(Position(
                            402, hit.position.y), hit.time, hit.hitsound,  hit.addition))
            progressbar_value += 100/len(self.osu._hit_objects)
            self.progressbar.setValue(progressbar_value)

    def save_file(self):
        if not self.tmp_hitobjects:
            QMessageBox.warning(self, '警告', '转换出现问题，请重试')
            return
        self.new_osu = Beatmap(format_version=self.osu.format_version,
                               audio_filename=self.osu.audio_filename,
                               audio_lead_in=self.osu.audio_lead_in,
                               preview_time=self.osu.preview_time,
                               countdown=self.osu.countdown, sample_set=self.osu.sample_set,
                               stack_leniency=self.osu.stack_leniency,
                               mode=self.osu.mode,
                               letterbox_in_breaks=self.osu.letterbox_in_breaks,
                               widescreen_storyboard=self.osu.widescreen_storyboard,
                               bookmarks=self.osu.bookmarks,
                               distance_spacing=self.osu.distance_spacing,
                               beat_divisor=self.osu.beat_divisor,
                               grid_size=self.osu.grid_size,
                               timeline_zoom=self.osu.timeline_zoom, title=self.osu.title,
                               title_unicode=self.osu.title_unicode,
                               artist=self.osu.artist, artist_unicode=self.osu.artist_unicode,
                               creator=self.osu.creator, version=self.osu.version,
                               source=self.osu.source, tags=self.osu.tags,
                               beatmap_id=self.osu.beatmap_id,
                               beatmap_set_id=self.osu.beatmap_set_id,
                               hp_drain_rate=self.osu.hp_drain_rate,
                               circle_size=self.osu.circle_size,
                               overall_difficulty=self.osu.overall_difficulty,
                               approach_rate=self.osu.approach_rate,
                               slider_multiplier=self.osu.slider_multiplier,
                               slider_tick_rate=self.osu.slider_tick_rate,
                               timing_points=self.osu.timing_points,
                               hit_objects=self.tmp_hitobjects)
        self.new_osu.circle_size = 7
        if self._1_3.isChecked():
            self.new_osu.version += ' 1_3'
        elif self._1_2.isChecked():
            self.new_osu.version += ' 1_2'
        elif self._2_3.isChecked():
            self.new_osu.version += ' 2_3'
        if self.lockhand:
            self.new_osu.version += ' lockhands'
        self.new_filename = path.join(path.dirname(
            self.filename), self.new_osu.display_name+'.osu')
        with open(self.new_filename, 'w', encoding='utf-8-sig') as f:
            self.new_osu.write_file(f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MainWin()
    mainwin.show()
    sys.exit(app.exec())
