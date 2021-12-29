import xlsxwriter as xls
import xlsxwriter.utility as xl_util
import pandas as pd
from datetime import date
import io

from cronoawp.core.awp_management import data_atual, cod_int_number_3dig, cod_int_number_4dig, cod_int_number_6dig, \
    get_string, filter_null_predecessor
from cronoawp.core.models import Wp_type , Standard_activities

#wb.define_name('area_grafico', f'=Graf!$N$8:INDEX(Graf!$1:$1048576,13,Graf!$M$8+13)')


def criar_planilha(output):
    wb = xls.Workbook(output)

    wp_type = wb.add_worksheet("wp_type")  # BD
    standard_activities = wb.add_worksheet("standard_activities")  # BD
    geral = wb.add_worksheet("geral")  # User
    cwa = wb.add_worksheet("cwa")  # User
    wp = wb.add_worksheet("wp")  # User

    planilha_wp_type(wp_type, wb)
    planilha_standard_activities(standard_activities, wb)
    planilha_general(general, wb)
    planilha_cwa(cwa, wb)
    planilha_wp(wp, wb)

    wb.close()


def planilha_wp_type(wp_type, wb):

    dados = Wp_type.objects.all()



    wp_type.add_table(xl_util.xl_range_abs(0, 0, dados.count(), 2),
                      {'name': 'wp_type7','style': None, 'columns': [{'header': 'sub_discipline'},
                                                       {'header': 'discipline'},
                                                       {'header': 'sub_discipline_id'}
                                                       ]})

    wp_type.write_row(0, 0, ['sub_discipline', 'discipline', 'sub_discipline_id'],
                      wb.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))


    row_num = 1

    for dado in dados:
        if row_num % 2 == 0:
            wp_type.write(row_num, 0, dado.sub_discipline)
            wp_type.write(row_num, 1, dado.discipline)
            wp_type.write(row_num, 2, dado.sub_discipline_id)
        else:
            wp_type.write(row_num, 0, dado.sub_discipline, wb.add_format({'bg_color': '#bfbfbf'}))
            wp_type.write(row_num, 1, dado.discipline, wb.add_format({'bg_color': '#bfbfbf'}))
            wp_type.write(row_num, 2, dado.sub_discipline_id, wb.add_format({'bg_color': '#bfbfbf'}))

        row_num += 1



    wp_type.hide_gridlines(2)
    wp_type.set_column('A:A', 60.71)
    wp_type.set_column('B:B', 23.00)
    wp_type.set_column('C:C', 20.00)
    wp_type.set_row(0, 40.0)
    wp_type.set_tab_color('green')




def planilha_standard_activities(standard_activities, wb):

    dados = Standard_activities.objects.all()



    standard_activities.add_table(xl_util.xl_range_abs(0, 0, dados.count(), 12),
                      {'name': 'standard_activities8','style': None, 'columns': [{'header': 'sub_discipline'},
                                                       {'header': 'work_package_type'},
                                                       {'header': 'project_phase'},
                                                       {'header': 'discipline'},
                                                       {'header': 'activity_name'},
                                                       {'header': 'standard_activities_id'},
                                                        {'header': 'predecessor'},
                                                        {'header': 'relation'},
                                                        {'header': 'lag'},
                                                        {'header': 'duration'},
                                                        {'header': 'physical_progress'},
                                                        {'header': 'financial_progress'},
                                                        {'header': 'responsible'},
                                                       ]})

    standard_activities.write_row(0, 0, ['sub_discipline', 'work_package_type', 'project_phase','discipline','activity_name',
                                         'standard_activities_id','predecessor','relation','lag','duration','physical_progress','financial_progress','responsible'],
                      wb.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))


    row_num = 1

    for dado in dados:
        if row_num % 2 == 0:
            standard_activities.write(row_num, 0, dado.sub_discipline)
            standard_activities.write(row_num, 1, dado.work_package_type)
            standard_activities.write(row_num, 2, dado.project_phase)
            standard_activities.write(row_num, 3, dado.discipline)
            standard_activities.write(row_num, 4, dado.activity_name)
            standard_activities.write(row_num, 5, dado.standard_activities_id)
            standard_activities.write(row_num, 6, dado.predecessor)
            standard_activities.write(row_num, 7, dado.relation)
            standard_activities.write(row_num, 8, dado.lag)
            standard_activities.write(row_num, 9, dado.duration)
            standard_activities.write(row_num, 10, dado.physical_progress)
            standard_activities.write(row_num, 11, dado.financial_progress)
            standard_activities.write(row_num, 12, dado.responsible)
        else:
            standard_activities.write(row_num, 0, dado.sub_discipline, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 1, dado.work_package_type, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 2, dado.project_phase, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 3, dado.discipline, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 4, dado.activity_name, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 5, dado.standard_activities_id, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 6, dado.predecessor, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 7, dado.relation, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 8, dado.lag, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 9, dado.duration, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 10, dado.physical_progress, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 11, dado.financial_progress, wb.add_format({'bg_color': '#bfbfbf'}))
            standard_activities.write(row_num, 12, dado.responsible, wb.add_format({'bg_color': '#bfbfbf'}))

        row_num += 1



    standard_activities.hide_gridlines(2)
    standard_activities.set_column('A:A', 62.14)
    standard_activities.set_column('B:B', 24.43)
    standard_activities.set_column('C:C', 38.00)
    standard_activities.set_column('D:D', 38.00)
    standard_activities.set_column('E:E', 111.71)
    standard_activities.set_column('F:F', 26.00)
    standard_activities.set_column('G:G', 16.71)
    standard_activities.set_column('H:H', 13.00)
    standard_activities.set_column('I:I', 13.00)
    standard_activities.set_column('J:J', 13.00)
    standard_activities.set_column('K:K', 22.14)
    standard_activities.set_column('L:L', 22.43)
    standard_activities.set_column('M:M', 16.29)
    standard_activities.set_row(0, 40.0)
    standard_activities.set_tab_color('green')



def planilha_general(geral, wb):


    geral.add_table(xl_util.xl_range_abs(0, 0, 1, 10),
                      {'name': 'general','style': 'Table Style Light 5', 'columns': [{'header': 'user_name'},
                                                       {'header': 'user_e-mail'},
                                                       {'header': 'verum_project_name'},
                                                       {'header': 'client_project_code'},
                                                       {'header': 'client_project_name'},
                                                       {'header': 'client_project_type'},
                                                        {'header': 'client_project_class'},
                                                        {'header': 'client_project_phase'},
                                                        {'header': 'client_project_step'},
                                                        {'header': 'client_project_state'},
                                                        {'header': 'version'},
                                                       ]})

    geral.write_row(0, 0, ['user_name', 'user_e-mail', 'verum_project_name','client_project_code','client_project_name',
                                         'client_project_type','client_project_class',
                             'client_project_phase','client_project_step','client_project_state','version'],
                      wb.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))

    geral.write_row(1, 0,['', '', '', '', '','', '', '', '', '', ''],
                      wb.add_format({'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))


    geral.hide_gridlines(2)
    geral.set_column('A:A', 16.00)
    geral.set_column('B:B', 26.00)
    geral.set_column('C:C', 25.57)
    geral.set_column('D:D', 23.71)
    geral.set_column('E:E', 24.57)
    geral.set_column('F:F', 23.43)
    geral.set_column('G:G', 23.86)
    geral.set_column('H:H', 24.86)
    geral.set_column('I:I', 23.14)
    geral.set_column('J:J', 24.14)
    geral.set_column('K:K', 8.43)
    geral.set_row(0, 40.0)
    geral.set_tab_color('orange')



def planilha_cwa(cwa, wb):


    cwa.add_table(xl_util.xl_range_abs(0, 0, 1, 8),
                      {'name': 'cwa','style': 'Table Style Light 5', 'columns': [{'header': 'client_project_name'},
                                                       {'header': 'project_area_id'},
                                                       {'header': 'project_area_name'},
                                                       {'header': 'cwa_name'},
                                                        {'header': 'cwa_description'},
                                                       {'header': 'cwa_code_1'},
                                                       {'header': 'cwa_code_2'},
                                                        {'header': 'cwa_code_3'},
                                                        {'header': 'version'}
                                                       ]})

    cwa.write_row(0, 0, ['client_project_name', 'project_area_id', 'project_area_name','cwa_name', 'cwa_description','cwa_code_1',
                                         'cwa_code_2','cwa_code_3', 'version'],
                      wb.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))

    cwa.write_row(1, 0,[cwa.data_validation('A2', {'validate': 'list', 'source': '=OFFSET(geral!$E$2,0,0,COUNTA(geral!E:E),1)'}), '', '', '', '','', '', ''],
                      wb.add_format({'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))


    cwa.hide_gridlines(2)
    cwa.set_column('A:A', 23.43)
    cwa.set_column('B:B', 26.00)
    cwa.set_column('C:C', 25.57)
    cwa.set_column('D:D', 23.71)
    cwa.set_column('E:E', 24.57)
    cwa.set_column('F:F', 23.43)
    cwa.set_column('G:G', 23.86)
    cwa.set_column('H:H', 24.86)
    cwa.set_column('I:I', 23.14)
    cwa.set_row(0, 40.0)
    cwa.set_tab_color('orange')


def planilha_wp(wp, wb):


    wp.add_table(xl_util.xl_range_abs(0, 0, 1, 9),
                      {'name': 'wp','style': 'Table Style Light 5', 'columns': [{'header': 'cwa_name'},
                                                       {'header': 'sub_discipline'},
                                                       {'header': 'discipline'},
                                                       {'header': 'work_package_description'},
                                                       {'header': 'tag'},
                                                       {'header': 'item_description'},
                                                        {'header': 'wp_code_1'},
                                                        {'header': 'wp_code_2'},
                                                        {'header': 'wp_code_3'},
                                                        {'header': 'version'}
                                                       ]})

    wp.write_row(0, 0, ['cwa_name', 'sub_discipline', 'discipline','work_package_description','tag',
                                         'item_description','wp_code_1','wp_code_2','wp_code_3', 'version'],
                      wb.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))

    wp.write_row(1, 0,[wp.data_validation('A2', {'validate': 'list', 'source': '=OFFSET(cwa!$D$2,0,0,COUNTA(cwa!D:D),1)'}), wp.data_validation('B2', {'validate': 'list', 'source': '=OFFSET(wp_type!$A$2,0,0,COUNTA(wp_type!A:A),1)'}), wp.data_validation('C2', {'validate': 'list', 'source': '=OFFSET(wp_type!$B$2,0,0,COUNTA(wp_type!B:B),1)'}), '', '','', '', '', '', ''],
                      wb.add_format({'align': 'center', 'valign': 'vcenter', 'font_size': '11'}))



    wp.hide_gridlines(2)
    wp.set_column('A:A', 28.71)
    wp.set_column('B:B', 25.86)
    wp.set_column('C:C', 23.71)
    wp.set_column('D:D', 56.29)
    wp.set_column('E:E', 10.00)
    wp.set_column('F:F', 56.29)
    wp.set_column('G:G', 56.29)
    wp.set_column('H:H', 56.29)
    wp.set_column('I:I', 56.29)
    wp.set_column('J:J', 8.43)
    wp.set_row(0, 40.0)
    wp.set_tab_color('orange')

### Importando


def gerar_cronograma(nova_planilha, output):

    run_awp(nova_planilha, output)



def run_awp(nova_planilha, output):
    ################################leitura das tabelas
    df_wp_type=pd.read_excel(nova_planilha, 'wp_type')
    df_standard_activities=pd.read_excel(nova_planilha, 'standard_activities')
    df_cwa=pd.read_excel(nova_planilha, 'cwa', converters={'project_area_id':str})
    df_wp=pd.read_excel(nova_planilha, 'wp')
    df_general=pd.read_excel(nova_planilha, 'general')

    ################################cwa_id
    df_cwa['linha'] = range(df_cwa.shape[0])
    sequencial_cwa = df_cwa.groupby("project_area_name")['linha'].rank("dense", ascending=True).apply(cod_int_number_3dig)
    df_cwa['cwa_id'] = df_cwa['project_area_id']+'-'+sequencial_cwa
    df_cwa = df_cwa.drop(['linha'],axis=1)

    df_cwa_1 = df_cwa.merge(df_general.drop(['version'],axis=1), how='left', on='client_project_name')
    df_cwa_1['created_by'] = df_cwa_1['user_name']
    df_cwa_1['updated_by'] = df_cwa_1['user_name']
    df_cwa_1['created_at'] = data_atual
    df_cwa_1['updated_at'] = data_atual
    df_cwa_1['version'] = df_cwa_1['version'].fillna(0)+1

    ################################wp_id
    cols_cwa = ['client_project_name',
                'project_area_id',
                'project_area_name',
                'cwa_id',
                'cwa_name',
                'cwa_description',
                'cwa_code_1',
                'cwa_code_2',
                'cwa_code_3',
                'created_at',
                'created_by',
                'updated_at',
                'updated_by']

    df_wp_item = (
                     df_wp
                     .merge(df_cwa_1[cols_cwa], how='left', on='cwa_name')
                     .merge(df_wp_type, how='left', on=['sub_discipline', 'discipline'])
                 )

    df_wp_item['linha'] = range(df_wp_item.shape[0])
    sequencial_wp = df_wp_item.groupby("cwa_name")['linha'].rank("dense", ascending=True).apply(cod_int_number_3dig)
    df_wp_item['wp_id'] = df_wp_item['cwa_id']+'-'+df_wp_item['sub_discipline_id']+'-'+sequencial_wp
    df_wp_item = df_wp_item.drop(['linha'],axis=1)

    ################################item__id
    df_wp_item['linha'] = range(df_wp_item.shape[0])
    sequencial_item = (
                          df_wp_item
                          .groupby("work_package_description")['linha']
                          .rank("dense", ascending=True)
                          .apply(cod_int_number_4dig)
                      )
    df_wp_item['item_id'] = df_wp_item['wp_id']+'-'+sequencial_item
    df_wp_item = df_wp_item.drop(['linha'],axis=1)

    cols_wp_item = ['item_id',
                    'wp_id',
                    'cwa_id',
                    'item_description',
                    'work_package_description',
                    'cwa_description',
                    'tag',
                    'sub_discipline',
                    'discipline',
                    'client_project_name',
                    'wp_code_1',
                    'wp_code_2',
                    'wp_code_3',
                    'created_at',
                    'created_by',
                    'updated_at',
                    'updated_by',
                    'version'
                   ]

    ################################activity_id
    cols_activity_id = ['activity_id',
                        'item_id',
                        'wp_id',
                        'cwa_id',
                        'activity_name',
                        'tag',
                        'work_package_type',
                        'project_phase',
                        'duration',
                        'item_description',
                        'work_package_description',
                        'sub_discipline',
                        'discipline',
                        'client_project_name',
                        'physical_progress',
                        'financial_progress',
                        'responsible',
                        'wp_code_1',
                        'wp_code_2',
                        'wp_code_3',
                        'created_at',
                        'created_by',
                        'updated_at',
                        'updated_by',
                        'version'
                       ]

    df_activitiy = (
                       df_wp_item[cols_wp_item]
                      .merge(df_wp_type, how='left', on=['discipline', 'sub_discipline'])
                      .merge(df_standard_activities, how='left', on=['discipline', 'sub_discipline'])
                   )

    linha = [cod_int_number_6dig(i) for i in range(1,df_activitiy.shape[0]+1)]
    df_activitiy['activity_id'] = (
        df_activitiy['cwa_id'].apply(get_string(4))+
        df_activitiy['sub_discipline_id']+
        '-'+
        linha+'-'+
        df_activitiy['standard_activities_id']
                                  )

    ################################predecessor_activity_id
    df_activitiy = df_activitiy.fillna({'predecessor': 'XXXXX'})
    linha = [cod_int_number_6dig(i) for i in range(1,df_activitiy.shape[0]+1)]
    df_activitiy['predecessor_activity_id'] = (
             df_activitiy['cwa_id'].apply(get_string(4))+
             df_activitiy['sub_discipline_id']+
             '-'+
             linha+'-'+
             df_activitiy['predecessor']
                                              )
    ################################df_relation
    cols = ['predecessor_activity_id', 'activity_id', 'relation', 'lag']
    index_filter = df_activitiy['predecessor_activity_id'].apply(filter_null_predecessor)
    df_relation = df_activitiy[cols][index_filter]
    df_relation.columns = ['predecessor_activity_id', 'sucessor_activity_id', 'relation', 'lag']

    ################################save tables
    excel_export = pd.ExcelWriter(output)
    df_cwa_1[cols_cwa+['version']].to_excel(excel_export,'cwa',index=False)
    df_wp_item[cols_wp_item].to_excel(excel_export,'wp_item',index=False)
    df_relation.to_excel(excel_export,'activity_relation',index=False)
    df_activitiy[cols_activity_id].to_excel(excel_export,'activity',index=False)
    excel_export.save()