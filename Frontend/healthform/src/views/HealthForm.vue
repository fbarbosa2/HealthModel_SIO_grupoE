<template>
  <div class="background">
    <div class="form-container">
      <h1>Formulário sobre a sua saúde</h1>
      <h2>Descubra a probabilidade de ter algum tipo de doença através do nosso modelo!</h2>

      <form @submit.prevent="handleSubmit">
        <div class="form-section">
          <h3>Dados Pessoais</h3>
          <div class="input-grid">
            <div class="input-card">
              <label for="age">Idade</label>
              <input type="number" v-model="form.age" id="age" min="0" required />
            </div>
            <div class="input-card">
              <label for="gender">Género</label>
              <select v-model="form.gender" id="gender">
                <option value="Male">Masculino</option>
                <option value="Female">Feminino</option>
              </select>
            </div>
            <div class="input-card">
              <label for="bp">Pressão Arterial</label>
              <select v-model="form.bp" id="bp">
                <option value="Normal">Normal</option>
                <option value="High">Alta</option>
                <option value="Low">Baixa</option>
              </select>
            </div>
            <div class="input-card">
              <label for="cholesterol">Colesterol</label>
              <select v-model="form.cholesterol" id="cholesterol">
                <option value="Low">Baixo</option>
                <option value="Normal">Normal</option>
                <option value="High">Alto</option>
              </select>
            </div>
          </div>
        </div>

        <div class="form-section">
          <h3>Sintomas</h3>
          <div class="input-grid">
            <div v-for="(label, key) in symptomFields" :key="key" class="input-card">
              <label :for="key">{{ label }}</label>
              <select v-model="form[key]" :id="key">
                <option value="Yes">Sim</option>
                <option value="No">Não</option>
              </select>
            </div>
          </div>
        </div>

        <button type="submit">Submeter</button>

        <div v-if="result" class="result-box">
          <div class="result-text">
            <strong>Diagnóstico previsto:</strong><br />
            <pre>{{ result }}</pre>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        fever: 'No',
        cough: 'No',
        fatigue: 'No',
        breathing: 'No',
        age: 0,
        gender: 'Male',
        bp: 'Normal',
        cholesterol: 'Normal',
        sore_throat: 'No',
        chest_pain: 'No',
        skin_rash: 'No',
        nausea: 'No',
        muscle_pain: 'No',
        loss_of_appetite: 'No',
        dizziness: 'No'
      },
      result: '',
      symptomFields: {
        fever: 'Febre',
        cough: 'Tosse',
        fatigue: 'Fadiga',
        breathing: 'Dificuldade Respiratória',
        sore_throat: 'Garganta Seca',
        chest_pain: 'Dor no Peito',
        skin_rash: 'Erupção Cutânea',
        nausea: 'Náuseas',
        muscle_pain: 'Dores Musculares',
        loss_of_appetite: 'Perda de Apetite',
        dizziness: 'Tonturas'
      }
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await fetch('http://localhost:5000/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        });
        const data = await response.json();
        this.result = data.result;
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
  background: linear-gradient(to right top, #141e30, #243b55);
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-container {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  border-radius: 20px;
  padding: 2rem;
  max-width: 900px;
  width: 100%;
  color: #ffffff;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.4);
  transition: all 0.3s ease-in-out;
}

h1 {
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

h2 {
  font-size: 1.1rem;
  margin-bottom: 2rem;
  text-align: center;
  color: #e0e0e0;
}

h3 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  margin-top: 1rem;
  color: #dcdcdc;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-section {
  margin-bottom: 2rem;
}

.input-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
}

.input-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 6px;
  box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.1);
  transition: background 0.3s ease;
}

label {
  font-weight: 600;
  font-size: 0.9rem;
}

input,
select {
  padding: 10px;
  border: none;
  border-radius: 8px;
  font-size: 0.95rem;
  background-color: rgba(255, 255, 255, 0.15);
  color: #fff;
  transition: background-color 0.3s;
}

input:focus,
select:focus {
  background-color: rgba(255, 255, 255, 0.25);
  outline: none;
}

button {
  align-self: center;
  padding: 12px 30px;
  background: linear-gradient(135deg, #00c6ff, #0072ff);
  border: none;
  color: white;
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  font-size: 1rem;
  box-shadow: 0 4px 15px rgba(0, 114, 255, 0.4);
  transition: background 0.3s ease;
}

button:hover {
  background: linear-gradient(135deg, #0072ff, #004cff);
}

.result-box {
  margin-top: 2rem;
  padding: 1.5rem;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(8px);
  color: #fff;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.2);
  animation: fadeIn 0.6s ease-in-out;
}

.result-text {
  font-size: 1.1rem;
  line-height: 1.5;
  font-family: 'Inter', sans-serif;
  white-space: pre-wrap;
}

select option {
  color: black;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>