#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

void countingSort(std::vector<int>& arr) {
    int max_element = *std::max_element(arr.begin(), arr.end());

    std::vector<int> count(max_element + 1, 0);
    std::vector<int> sorted_arr(arr.size());

    for (int num : arr) {
        ++count[num];
    }

    for (int i = 1; i <= max_element; ++i) {
        count[i] += count[i - 1];
    }

    for (int i = arr.size() - 1; i >= 0; --i) {
        sorted_arr[count[arr[i]] - 1] = arr[i];
        --count[arr[i]];
    }

    arr = sorted_arr;
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
        countingSort(lista_numeros);
        auto fin = std::chrono::high_resolution_clock::now();
        
        double tiempo = std::chrono::duration_cast<std::chrono::microseconds>(fin - inicio).count();
        tiempos.push_back(tiempo);
        
        inputFile.close();
        std::cout << tiempo/1000000 << std::endl;
    }
    
    std::ofstream outputFile("tiempos_counting_sort.txt");
    for (double tiempo:tiempos){
        outputFile<<tiempo/1000000<< " ";
    }
    outputFile.close();
    
    std::cout<<"Fin"<<std::endl;
    return 0;
}