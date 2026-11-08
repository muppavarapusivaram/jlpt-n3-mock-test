// app/src/App.jsx
import React, { useState } from 'react';
import HomeView from './components/HomeView';
import ExamView from './components/ExamView';
import ResultsView from './components/ResultsView';
import BankExplorerModal from './components/BankExplorerModal';
import SakuraPetals from './components/SakuraPetals';
import { generateBalancedMockTest } from './services/mockTestAlgorithm';

export default function App() {
  const [currentView, setCurrentView] = useState('home'); // 'home' | 'exam' | 'results'
  const [activeExam, setActiveExam] = useState(null);
  const [examMode, setExamMode] = useState('official');
  const [userAnswers, setUserAnswers] = useState({});
  const [isExplorerOpen, setIsExplorerOpen] = useState(false);

  // Start exam from HomeView
  const handleStartExam = (exam, mode) => {
    setActiveExam(exam);
    setExamMode(mode);
    setUserAnswers({});
    setCurrentView('exam');
  };

  // Exam finished -> Go to results
  const handleFinishExam = (exam, answers) => {
    setUserAnswers(answers);
    setCurrentView('results');
  };

  // Retake same exam
  const handleRetakeExam = () => {
    setUserAnswers({});
    setCurrentView('exam');
  };

  // Shuffle & Generate new exam immediately
  const handleGenerateAndStartNew = () => {
    const newTest = generateBalancedMockTest();
    setActiveExam(newTest);
    setUserAnswers({});
    setCurrentView('exam');
  };

  // Return to home
  const handleGoHome = () => {
    setCurrentView('home');
  };

  return (
    <div className="app-root" style={{ position: 'relative', minHeight: '100vh' }}>
      {/* Floating Japanese Sakura Cherry Blossom Petals */}
      <SakuraPetals />

      {/* Main View Router */}
      <div style={{ position: 'relative', zIndex: 1 }}>
        {currentView === 'home' && (
          <HomeView
            onStartExam={handleStartExam}
            onOpenExplorer={() => setIsExplorerOpen(true)}
          />
        )}

        {currentView === 'exam' && activeExam && (
          <ExamView
            exam={activeExam}
            mode={examMode}
            onFinishExam={handleFinishExam}
            onExit={handleGoHome}
          />
        )}

        {currentView === 'results' && activeExam && (
          <ResultsView
            exam={activeExam}
            userAnswers={userAnswers}
            onRetake={handleRetakeExam}
            onNewExam={handleGenerateAndStartNew}
            onGoHome={handleGoHome}
          />
        )}

        {isExplorerOpen && (
          <BankExplorerModal onClose={() => setIsExplorerOpen(false)} />
        )}
      </div>
    </div>
  );
}
