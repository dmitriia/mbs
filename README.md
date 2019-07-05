
<div align="center">
 <img width=12%, height=12%, src="logo.JPG"><br><br>
</div>

# Модель ценообразования ипотечных ценных бумаг

Проект состоит из набора скриптов и модулей, реализующих модель оценки однотраншевых ипотечных ценных бумаг (ИЦБ).

В проекте представлена демонстрационная версия кода модели и некоторых ее общих настроек, предназначенная для ознакомления с методами оценок ИЦБ. Результаты расчетов с использованием проекта являются индикативными и не должны рассматриваться пользователями в качестве замены проведения ими самостоятельного анализа. Результаты расчетов, полученные с использованием проекта, не могут быть использованы в качестве заверения о том, что какая-либо определенная сделка непременно могла быть или может быть осуществлена по определенной цене, либо с определенной доходностью.

****

## Логическая структура

Проект состоит из нескольких блоков:

 - **Импорт данных** из внешних источников (историческое погашение облигаций, данные макроэкономики);
 - **Валидация и подготовка данных** о покрытии ИЦБ (LLD);
 - **Моделирование процентной ставки и макроэкономических показателей** с использованием симуляций;
 - **Построение денежных потоков** по портфелю закладных, соответствующих реализациям макроэкономических показателей;
 - **Структурирование денежных потоков** по пулу в прогнозные потоки по ИЦБ (транширование);
 - **Оценка приведенной стоимости** потоков и расчет основных метрик ИЦБ.


## Среда разработки

Проект реализован на языке программирования **Python (версии 2.7.14)** с использованием внешних библиотек:

- Numpy 1.14.1

- Pandas 0.22.0

- Scipy 1.0.0

Предполагается, что основные скрипты проекта могут быть использованы как самостоятельные программы, например, вызовом из командной строки с передачей параметров, так и в качестве импортируемых модулей вызовом из других скриптов Python.

## Структура файлов модели

### Скрипты
[runner.py](https://github.com/domrf/mbs_pricing/blob/master/runner.py) - основной скрипт, который позволяет провести комплексную **оценку стоимости** ценной бумаги и сопутствующих показателей. 

[pricing.py](https://github.com/domrf/mbs_pricing/blob/master/pricing.py) - вспомогательный скрипт, который позволяет создать **json-файл с входными параметрами** модели.

[reader.py](https://github.com/domrf/mbs_pricing/blob/master/reader.py) - вспомогательный скрипт, который позволяет провести **проверку** корректного заполнения входного LLD.

### Модули

#### **[model](https://github.com/domrf/mbs_pricing/tree/master/model)**
Основной модуль с системными файлами модели. Состоит из набора логически независимых моделей, в последовательности их применения:

 1. [model_lld](https://github.com/domrf/mbs_pricing/blob/master/model/model_lld.py) - **кластеризация входных данных** по закладным;
 2. [model_cir](https://github.com/domrf/mbs_pricing/blob/master/model/model_cir.py) - **моделирование процентных ставок и макроэкономических показателей**, необходимых для расчета денежных потоков;
 3. [model_cfm](https://github.com/domrf/mbs_pricing/blob/master/model/model_cfm.py) - **прогноз денежных потоков по пулу закладных** в результате моделирования поведения заемщиков и жизненного цикла пула;
 4. [model_mbs](https://github.com/domrf/mbs_pricing/blob/master/model/model_mbs.py) - **структурирование** и оценка денежных потоков по ИЦБ.


#### **[impdata](https://github.com/domrf/mbs_pricing/tree/master/impdata)**
Вспомогательный модуль с необходимыми для проведения оценок **внешними данными**:

 1. [gparams.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/gparams.py) – исторические данные для параметризации КБД; 
 2. [histcf.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/histcf.py) – исторические данные по амортизации и купонным выплатам ИЦБ;
 3. [history.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/history.py) – исторические данные макропоказателей;
 4. [hpi.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/hpi.py) – исторические данные индекса цен на недвижимость;
 5. [mbs.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/mbs.py) – перечень основных параметров ИЦБ;
 6. [regions.py](https://github.com/domrf/mbs_pricing/blob/master/impdata/regions.py) – справочник кодов регионов.

#### **[specs](https://github.com/domrf/mbs_pricing/tree/master/specs)**
Вспомогательный модуль с настройками различных **моделей миграций**.

### Данные с примерами
[examples](https://github.com/domrf/mbs_pricing/tree/master/examples) - **набор примеров входных данных** по закладным в составе ИЦБ.

****

## Пример запуска модели

В качестве примера реализована возможность оценки стоимости двух ИЦБ, с фиксированным и плавающим купоном соответственно: [RU000A0ZYJT2](https://www.moex.com/ru/issue.aspx?board=TQOD&code=RU000A0ZYJT2) (оригинатор – банк ВТБ), [выпущенной](https://mbsfactory.ahml.ru/tsennaya-bumaga-4-02-00307-r-002p/) в рамках проекта ДОМ.<span>РФ «Фабрика ИЦБ», и [RU000A0ZYL89](https://www.moex.com/ru/issue.aspx?board=TQOD&code=RU000A0ZYL89) (оригинатор – Райффайзенбанк), аналогично [выпущенной](https://mbsfactory.ahml.ru/tsennaya-bumaga-4-03-00307-r-002p/) в рамках Фабрики.

Дата оценки – 15 апреля 2019. Процесс оценивания выстроен согласно следующей логике (для удобства команды запуска собраны в файлах runme.bat в папках примеров):

1. Оценка осуществляется путем запуска скрипта **runner.<span>py**, который принимает на вход _json_-файл с параметрами модели и облигации, а также _csv_-файл с данными по ближайшему к дате оценки срезу портфеля закладных (loan-level data, LLD). В примере представлен LLD на 1 апреля 2019, в папке **examples**.

2. При запуске **runner.<span>py** сначала проводится валидация данных LLD. По завершении исправления ошибок будет проведена процедура кластеризации портфеля.

3. На первом шаге моделирования запускается блок макроэкономики (**model_cir.py**), который создает сценарные симуляции короткой ставки, доходности, а также макроэкономических показателей: ставки МосПрайм 6-мес., ставки по ипотеке, индекса цен на недвижимость. Количество сценариев определяется параметром ‘NumberOfMonteCarloSimulations’ в json-файле, горизонт моделирования - параметром ‘ModelingHorizon’. Переменные симулируются помесячно.

4. Второй шаг моделирования – блок модели досрочных погашений (**model_cfm.py**), в котором для каждого макро-сценария моделируется жизнь портфеля закладных, входящих в обеспечение ИЦБ: остаток основного долга в портфеле на каждый месяц, помесячные поступления по процентам, помесячные досрочные погашения, и т.д.

5. Третий шаг моделирования реализован в скрипте **model_mbs.py**: для каждого макро-сценария на основе результатов блока модели досрочных погашений производится расчет всех будущих денежных потоков по облигации (купонных выплат и погашений номинала). Для каждого макро-сценария оценка текущей стоимости ИЦБ будет рассчитана как сумма дисконтированных денежных потоков, где в качестве ставки дисконтирования выступит сценарная ставка доходности. Как следствие, будет получено эмпирическое распределение оценки текущей цены, среднее по которому даст оценку ИЦБ.

6. В калькуляторе по умолчанию проводятся три варианта оценки: «центральный» - для указанных значений КБД (кривой бескупонной доходности) на дату оценки, а также два «стрессированных» - для сдвига текущей КБД вниз на 100 б.п. и вверх на 100 б.п.

7. По окончании работы скрипта **runner.<span>py** в папке c LLD данными будут сохранены все промежуточные и финальные результаты моделирования (в формате csv):

- **temp_LLD,** **stat_LLD**, **data_LLD** – исправленные данные по срезу портфеля, необходимая статистика по срезу, результат кластеризации портфеля соответственно;

- **macroscr_central**, **macroscr_m100bp**, **macroscr_p100bp** – результирующие таблицы блока макроэкономики для трех вариантов оценки («центральный», «минус 100 б.п.» и «плюс 100 б.п.» соответственно);

- **cashflow_central**, **cashflow_m100bp**, **cashflow_p100bp** – результирующие таблицы блока модели досрочных погашений для трех вариантов оценки;

- **mbsflows_central**, **mbsflows_m100bp**, **mbsflows_p100bp** - результирующие таблицы блока транширования (расчета будущих денежных потоков по бумаге) для трех вариантов оценки;

- **pricing_result** – общая таблица с основными результатами оценивания для трех вариантов; включает в себя средние по симуляциям грязные/чистые цены ИЦБ, а также дополнительные статистики: IRR при грязной цене, дюрация Маколея, модифицированная дюрация, эффективная дюрация, выпуклость и CPR.

****
