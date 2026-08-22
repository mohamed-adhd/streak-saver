using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Controls;
using Avalonia.Interactivity;
using ssaver.Models;
namespace ssaver.ViewModels;


public partial class configsViewModel : ViewModelBase
{
    [ObservableProperty] private MainWindowViewModel _main;
    [ObservableProperty] public string username;
    [ObservableProperty] public string repoName;
    [ObservableProperty] public string filePath;
    [ObservableProperty] public string token;
    private Api s =new Api(); 
    public configsViewModel(MainWindowViewModel main)
    {
        _main = main;
    }
    [RelayCommand]
    private void onVerifyClicked()
    {
        s.send(Username,RepoName,FilePath,Token);
        _main.Current_page = new DoneViewModel();
    }
}
