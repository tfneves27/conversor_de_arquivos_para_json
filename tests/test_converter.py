from src.converter import convert_csv_to_json, convert_excel_to_json, convert_docx_to_json, convert_file
import os
import pytest
# --- Teste para a função de CSV
def test_convert_csv_to_json_success():
    # 1. Arrange
    csv_file_path = os.path.join('tests', 'data', 'sample1.csv')
    expected_json = '{"id":{"0":1,"1":2},"name":{"0":"test","1":"python"}}'

    # 2. Act
    actual_json = convert_csv_to_json(csv_file_path)

    # 3. Assert
    assert actual_json == expected_json

# --- Teste para a função de Excel
def test_convert_excel_to_json_success():
    # 1. Arrange
    excel_file_path = os.path.join('tests', 'data', 'sample2.xlsx')
    expected_json = '{"id":{"0":1,"1":2},"name":{"0":"excel","1":"pandas"}}'
    
    # 2. Act
    actual_json = convert_excel_to_json(excel_file_path)

    # 3. Assert
    assert actual_json == expected_json

# --- Teste para a função de World
def test_convert_docx_to_json_sucess():
    # 1. Arrange
    docx_file_path = os.path.join('tests', 'data', 'sample3.docx')
    expected_json = '["teste de python", "teste arquivo .docx", "fim"]'

    # 2. Act
    actual_json = convert_docx_to_json(docx_file_path)

    # 3. Assert
    assert actual_json == expected_json

def test_convert_file_unsupported_extension_raise_error():
    txt_file_path = os.path.join('tests', 'data', 'sample4.txt')

    with pytest.raises(ValueError): 
        convert_file(txt_file_path)
       