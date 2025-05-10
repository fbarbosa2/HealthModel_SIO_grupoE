<template>
  <div class="background">
    <div class="form-container">
      <h1>Formulário de Sintomas</h1>
      <h2>Selecione os sintomas que costuma a sentir:</h2>
      <form @submit.prevent="handleSubmit">
        <template v-for="sintoma in sintomas" :key="sintoma">
          <label :for="sintoma">{{ sintomasPt[sintoma] }}</label>
          <select v-model="form[sintoma]" :id="sintoma">
            <option value="No">Não</option>
            <option value="Yes">Sim</option>
          </select>
        </template>

        <button type="submit">Submeter</button>

        <p v-if="result" class="result">{{ result }}</p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sintomas: [
        'fever', 'fatigue', 'headache', 'nausea', 'vomiting',
        'dizziness', 'chills', 'weakness', 'sweating',
        'cough', 'sore throat',
        'abdominal pain', 'bloating',
        'frequent urination', 'blood in urine',
        'joint pain', 'muscle pain',
        'sleepiness', 'memory problems',
        'anxiety and nervousness', 'depression'
      ],
      sintomasPt: {
        fever: 'Febre',
        fatigue: 'Fadiga',
        headache: 'Dor de cabeça',
        nausea: 'Náusea',
        vomiting: 'Vómitos',
        dizziness: 'Tonturas',
        chills: 'Calafrios',
        weakness: 'Fraqueza',
        sweating: 'Suores',
        cough: 'Tosse',
        'sore throat': 'Dor de garganta',
        'abdominal pain': 'Dor abdominal',
        bloating: 'Inchaço abdominal',
        'frequent urination': 'Urinação frequente',
        'blood in urine': 'Sangue na urina',
        'joint pain': 'Dor nas articulações',
        'muscle pain': 'Dor muscular',
        sleepiness: 'Sonolência',
        'memory problems': 'Problemas de memória',
        'anxiety and nervousness': 'Ansiedade e nervosismo',
        depression: 'Depressão'
      },
      form: {},
      result: ''
    };
  },
  created() {
    this.sintomas.forEach(s => {
      this.form[s] = 'No';
    });
  },
  methods: {
    async handleSubmit() {
      try {
        const sintomasSelecionados = Object.keys(this.form).filter(
          s => this.form[s] === 'Yes'
        );

        const response = await fetch('http://localhost:5000/predict-complex', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ sintomas: sintomasSelecionados })
        });

        const data = await response.json();

        if (data.result) {
          const [doenca, certeza] = data.result.split(' - ');
          this.result = `${doenca} - ${certeza}`;
        } else {
          this.result = 'Erro ao obter diagnóstico.';
        }
      } catch (error) {
        console.error('Erro ao submeter:', error);
        this.result = 'Erro ao obter diagnóstico.';
      }
    }
  }
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.background {
  min-height: 100vh;
  background: linear-gradient(135deg, #1e3c72 0%, #3360ad 50%, #6ca7ce 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-container {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  border-radius: 20px;
  padding: 2rem;
  width: 100%;
  max-width: 700px;
  color: #fff;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
  margin-top: 20px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #ffffff;
}

h2 {
  font-size: 1rem;
  margin-bottom: 1.5rem;
  color: #e9e6e6;
}

form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

label {
  font-weight: 600;
  margin-top: 0.5rem;
}

select {
  padding: 10px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
  transition: background-color 0.3s;
}

select:focus {
  background-color: rgba(255, 255, 255, 0.3);
  outline: none;
}

button {
  margin-top: 1rem;
  padding: 12px;
  background: linear-gradient(135deg, #2196f3, #1e88e5);
  border: none;
  color: white;
  font-weight: 600;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background: linear-gradient(135deg, #1976d2, #1565c0);
}

.result {
  margin-top: 1rem;
  font-weight: bold;
  font-size: 1.1rem;
  color: #ffffff;
}

select option {
  color: black;
}
</style>
