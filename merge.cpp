#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> left_arr(n1);
    std::vector<int> right_arr(n2);

    for (int i = 0; i < n1; ++i) {
        left_arr[i] = arr[left + i];
    }

    for (int j = 0; j < n2; ++j) {
        right_arr[j] = arr[mid + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (left_arr[i] <= right_arr[j]) {
            arr[k] = left_arr[i];
            ++i;
        } else {
            arr[k] = right_arr[j];
            ++j;
        }
        ++k;
    }

    while (i < n1) {
        arr[k] = left_arr[i];
        ++i;
        ++k;
    }

    while (j < n2) {
        arr[k] = right_arr[j];
        ++j;
        ++k;
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    std::string folderPath = "C:\\ADA\\todo\\"; 
    std::vector<int> cantidades = {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    std::vector<double> tiempos;

    for (int v : cantidades) {
        std::string filePath = folderPath + std::to_string(v) + ".txt";
        std::ifstream inputFile(filePath);
        if (!inputFile) {
            std::cerr << "Archivo no encontrado: " << filePath << std::endl;
            continue;
        }
        
        std::vector<int> lista_numeros;
        int numero;
        while (inputFile >> numero) {
            lista_numeros.push_back(numero);
        }
        
        auto inicio = std::chrono::high_resolution_clock::now();
        mergeSort(lista_numeros, 0, lista_numeros.size() - 1);
        auto fin = std::chrono::high_resolution_clock::now();
        double tiempo = std::chrono::duration_cast<std::chrono::microseconds>(fin - inicio).count();
        tiempos.push_back(tiempo);
        inputFile.close();
        std::cout << tiempo/1000000 << std::endl;
    }
    std::ofstream outputFile("tiempos_merge_sort.txt");
    for (double tiempo : tiempos) {
        outputFile << tiempo / 1000000 << " ";
    }
    outputFile.close();
    std::cout << "Fin" << std::endl;
    return 0;
}