{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNMcZ9bsEQR2T1t2n1Eic1N",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/2303A51453/sampelly-suhas/blob/main/lab_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('list')\n",
        "l=[10,99.9,\"cse\"]\n",
        "for i in l:\n",
        "    print(type(i),i)\n",
        "li=[10,20,30,40]\n",
        "print(li)\n",
        "if 20 in li:\n",
        "    print('found')\n",
        "else:\n",
        "    print('not found')\n",
        "li.append(50)\n",
        "print(li)\n",
        "li.remove(30)\n",
        "print(li)\n",
        "li.insert(2,25)\n",
        "print(li)\n",
        "l.pop()\n",
        "lis=[9,3,10,40,5,0]\n",
        "lis.reverse()\n",
        "print(lis)\n",
        "lis.sort()\n",
        "print(lis)\n",
        "print(sum(lis))\n",
        "print(max(lis))\n",
        "print(min(lis))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l-14BWTiFQ82",
        "outputId": "cbd4b32e-9870-40e9-91d6-6a0f82da310d"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "list\n",
            "<class 'int'> 10\n",
            "<class 'float'> 99.9\n",
            "<class 'str'> cse\n",
            "[10, 20, 30, 40]\n",
            "found\n",
            "[10, 20, 30, 40, 50]\n",
            "[10, 20, 40, 50]\n",
            "[10, 20, 25, 40, 50]\n",
            "[0, 5, 40, 10, 3, 9]\n",
            "[0, 3, 5, 9, 10, 40]\n",
            "67\n",
            "40\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BhBzLJFm5j9r",
        "outputId": "548b2ef2-bc20-46c0-a835-7c94250f36e0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10, 20, 30, 40, 50]\n",
            "[10, 20, 30, 40, 50]\n",
            "<class 'int'> 10\n",
            "<class 'float'> 99.9\n",
            "<class 'str'> cse\n",
            "not f\n",
            "3\n",
            "6\n",
            "(10, 20, 30, 40, 50)\n",
            "((10, 20), (30, 40), (40, 50), (50, 60))\n"
          ]
        }
      ],
      "source": [
        "# List printing\n",
        "t = [10, 20, 30, 40, 50]\n",
        "print(t)\n",
        "\n",
        "t = [10, 20, 30, 40, 50]\n",
        "print(t)\n",
        "\n",
        "# Mixed list with types\n",
        "t = [10, 99.9, 'cse']\n",
        "for i in t:\n",
        "    print(type(i), i)\n",
        "\n",
        "# Membership check\n",
        "if 20 in t:\n",
        "    print('f')\n",
        "else:\n",
        "    print('not f')\n",
        "\n",
        "t = (1, 2, 3, 2, 3, 2, 4)\n",
        "print(t.count(2))\n",
        "print(t.index(4))\n",
        "\n",
        "# Convert list to tuple\n",
        "l = [10, 20, 30, 40, 50]\n",
        "mytuple = tuple(l)\n",
        "print(mytuple)\n",
        "\n",
        "# Nested tuples\n",
        "student = ((10, 20), (30, 40), (40, 50), (50, 60))\n",
        "print(student)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "student = {'name': 'Suhas', 'id': '101', 'branch': 'cse'}\n",
        "# Correct way to print keys, values, items\n",
        "print(student.keys())\n",
        "print(student.values())\n",
        "print(student.items())\n",
        "\n",
        "# Correct loop over keys and values\n",
        "for key, value in student.items():\n",
        "    print(key, value)\n",
        "\n",
        "# Add a new key-value pair\n",
        "student['college'] = 'SRU'\n",
        "\n",
        "# Update dictionary\n",
        "student.update({'year': '2nd'})\n",
        "print(student)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GeVTxesP-sxG",
        "outputId": "94266c17-275d-4723-cf5b-a3a08e6391fa"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dict_keys(['name', 'id', 'branch'])\n",
            "dict_values(['Suhas', '101', 'cse'])\n",
            "dict_items([('name', 'Suhas'), ('id', '101'), ('branch', 'cse')])\n",
            "name Suhas\n",
            "id 101\n",
            "branch cse\n",
            "{'name': 'Suhas', 'id': '101', 'branch': 'cse', 'college': 'SRU', 'year': '2nd'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l = [[10, 20], [30, 40], [50, 60]]\n",
        "\n",
        "for i in l:\n",
        "    print(*i)\n",
        "\n",
        "print('10\\t20\\n30\\t40\\n50\\t60')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z_Qx7mNDC_R6",
        "outputId": "7b491eeb-b59e-4512-eec1-76e94b8ecd66"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 20\n",
            "30 40\n",
            "50 60\n",
            "10\t20\n",
            "30\t40\n",
            "50\t60\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Initial sets\n",
        "S = {1, 2, 3, 4}\n",
        "print(S)\n",
        "\n",
        "S = {1, 2, 3, 2, 3, 2}\n",
        "print(S)  # duplicates removed\n",
        "\n",
        "# Loop and membership check\n",
        "for i in S:\n",
        "    print(i)\n",
        "\n",
        "if 2 in S:\n",
        "    print('f')\n",
        "else:\n",
        "    print('not f')\n",
        "\n",
        "# Adding frozenset instead of set\n",
        "S = {1, 2, 3, 4}\n",
        "S.add(frozenset({5, 6}))\n",
        "print(S)\n",
        "\n",
        "# Removing element\n",
        "S = {1, 2, 3, 4}\n",
        "S.remove(2)\n",
        "print(S)\n",
        "\n",
        "# Clearing set\n",
        "S = {1, 2, 3, 4}\n",
        "S.clear()\n",
        "print(S)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PHc1HJKhFXYm",
        "outputId": "2dbea9ec-651b-4a3b-f1e3-4b7333c9f4dd"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1, 2, 3, 4}\n",
            "{1, 2, 3}\n",
            "1\n",
            "2\n",
            "3\n",
            "f\n",
            "{1, 2, 3, 4, frozenset({5, 6})}\n",
            "{1, 3, 4}\n",
            "set()\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "# 1. Create a 2D NumPy array for student marks in 3 subjects (rows: students, cols: subjects)\n",
        "marks = np.array([\n",
        "    [78, 85, 92],\n",
        "    [56, 64, 70],\n",
        "    [89, 90, 94],\n",
        "    [72, 75, 80],\n",
        "    [95, 98, 99]\n",
        "])\n",
        "\n",
        "print(\"Original Marks Array:\\n\", marks)\n",
        "\n",
        "# 2. Calculate average, minimum, and maximum marks\n",
        "avg_marks = np.mean(marks)\n",
        "min_marks = np.min(marks)\n",
        "max_marks = np.max(marks)\n",
        "\n",
        "print(\"\\nAverage Marks:\", avg_marks)\n",
        "print(\"Minimum Marks:\", min_marks)\n",
        "print(\"Maximum Marks:\", max_marks)\n",
        "\n",
        "# 3. Use slicing to retrieve marks of specific students (e.g., 2nd and 4th students)\n",
        "specific_students = marks[[1, 3], :]  # Row indices 1 and 3\n",
        "print(\"\\nMarks of 2nd and 4th Students:\\n\", specific_students)\n",
        "\n",
        "# 4. Boolean indexing to find students scoring above 80 in any subject\n",
        "above_80 = marks > 80\n",
        "print(\"\\nBoolean Mask for Marks > 80:\\n\", above_80)\n",
        "print(\"\\nMarks above 80:\\n\", marks[above_80])\n",
        "\n",
        "# 5. Reshape the array to observe subject-wise performance\n",
        "# Currently shape: (5 students, 3 subjects) → Reshape to (3 subjects, 5 students)\n",
        "subject_wise = marks.T\n",
        "print(\"\\nSubject-wise Performance:\\n\", subject_wise)\n",
        "\n",
        "# 6. Brief Analysis\n",
        "print(\"\\nAnalysis:\")\n",
        "print(\"- The highest score is\", max_marks, \"and the lowest is\", min_marks)\n",
        "print(\"- Student 5 has consistently high marks in all subjects.\")\n",
        "print(\"- Subject 3 shows the highest average performance overall.\")\n",
        "print(\"- Boolean indexing shows many students exceed 80 in Subject 3.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qZ-SrAvcLhou",
        "outputId": "14f7656a-c4c9-4304-8d4a-db604b11deb0"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original Marks Array:\n",
            " [[78 85 92]\n",
            " [56 64 70]\n",
            " [89 90 94]\n",
            " [72 75 80]\n",
            " [95 98 99]]\n",
            "\n",
            "Average Marks: 82.46666666666667\n",
            "Minimum Marks: 56\n",
            "Maximum Marks: 99\n",
            "\n",
            "Marks of 2nd and 4th Students:\n",
            " [[56 64 70]\n",
            " [72 75 80]]\n",
            "\n",
            "Boolean Mask for Marks > 80:\n",
            " [[False  True  True]\n",
            " [False False False]\n",
            " [ True  True  True]\n",
            " [False False False]\n",
            " [ True  True  True]]\n",
            "\n",
            "Marks above 80:\n",
            " [85 92 89 90 94 95 98 99]\n",
            "\n",
            "Subject-wise Performance:\n",
            " [[78 56 89 72 95]\n",
            " [85 64 90 75 98]\n",
            " [92 70 94 80 99]]\n",
            "\n",
            "Analysis:\n",
            "- The highest score is 99 and the lowest is 56\n",
            "- Student 5 has consistently high marks in all subjects.\n",
            "- Subject 3 shows the highest average performance overall.\n",
            "- Boolean indexing shows many students exceed 80 in Subject 3.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# 1. Create a pandas DataFrame from a dictionary\n",
        "data = {\n",
        "    'Name': ['Mithran', 'Suhas', 'lokesh', 'Dhanush', 'saishran'],\n",
        "    'ID': [101, 102, 103, 104, 105],\n",
        "    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing'],\n",
        "    'Salary': [48000, 55000, 72000, 46000, 60000]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "print(\"Original DataFrame:\\n\", df, \"\\n\")\n",
        "\n",
        "# 2. Filter employees with salary > 50,000\n",
        "high_salary = df[df['Salary'] > 50000]\n",
        "print(\"Employees with Salary > 50,000:\\n\", high_salary, \"\\n\")\n",
        "\n",
        "# 3. Sort the DataFrame by salary in descending order\n",
        "sorted_df = df.sort_values(by='Salary', ascending=False)\n",
        "print(\"DataFrame Sorted by Salary (Descending):\\n\", sorted_df, \"\\n\")\n",
        "\n",
        "# 4. Add a new column for Bonus (10% of salary)\n",
        "df['Bonus'] = df['Salary'] * 0.10\n",
        "print(\"DataFrame with Bonus Column:\\n\", df, \"\\n\")\n",
        "\n",
        "# 5. Calculate total salary expense including bonuses\n",
        "df['Total_with_Bonus'] = df['Salary'] + df['Bonus']\n",
        "total_expense = df['Total_with_Bonus'].sum()\n",
        "print(\"Total Salary Expense (including bonuses):\", total_expense, \"\\n\")\n",
        "\n",
        "# 6. Save the DataFrame to a CSV file\n",
        "df.to_csv('employee_salary_with_bonus.csv', index=False)\n",
        "print(\"Data saved to 'employee_salary_with_bonus.csv'\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_b5bppMHT6PP",
        "outputId": "66e07c51-10db-4160-a248-276cb4332d78"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original DataFrame:\n",
            "        Name   ID Department  Salary\n",
            "0   Mithran  101         HR   48000\n",
            "1     Suhas  102         IT   55000\n",
            "2    lokesh  103    Finance   72000\n",
            "3   Dhanush  104         IT   46000\n",
            "4  saishran  105  Marketing   60000 \n",
            "\n",
            "Employees with Salary > 50,000:\n",
            "        Name   ID Department  Salary\n",
            "1     Suhas  102         IT   55000\n",
            "2    lokesh  103    Finance   72000\n",
            "4  saishran  105  Marketing   60000 \n",
            "\n",
            "DataFrame Sorted by Salary (Descending):\n",
            "        Name   ID Department  Salary\n",
            "2    lokesh  103    Finance   72000\n",
            "4  saishran  105  Marketing   60000\n",
            "1     Suhas  102         IT   55000\n",
            "0   Mithran  101         HR   48000\n",
            "3   Dhanush  104         IT   46000 \n",
            "\n",
            "DataFrame with Bonus Column:\n",
            "        Name   ID Department  Salary   Bonus\n",
            "0   Mithran  101         HR   48000  4800.0\n",
            "1     Suhas  102         IT   55000  5500.0\n",
            "2    lokesh  103    Finance   72000  7200.0\n",
            "3   Dhanush  104         IT   46000  4600.0\n",
            "4  saishran  105  Marketing   60000  6000.0 \n",
            "\n",
            "Total Salary Expense (including bonuses): 309100.0 \n",
            "\n",
            "Data saved to 'employee_salary_with_bonus.csv'\n"
          ]
        }
      ]
    }
  ]
}